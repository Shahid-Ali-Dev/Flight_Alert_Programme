
from dateutil.parser import parse
from data_manager import DataManager
import inflect
import time
import requests
from notification_manager import NotificationManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

data = DataManager()
flight_search = FlightSearch()
sheet_auth = data.header
notifier = NotificationManager()

for i in data.sheet_data:
    headers = {"Authorization": f"Bearer {flight_search.token}"}

    # Get IATA code if missing
    if i["iataCode"] == "":
        time.sleep(1.3)
        params = {"keyword": i["city"], "subType": "CITY,AIRPORT"}
        response = requests.get("https://test.api.amadeus.com/v1/reference-data/locations", params=params,
                                headers=headers).json()
        if response.get("data"):
            i["iataCode"] = response["data"][0]["iataCode"]
            data.put({"price": {"iataCode": i["iataCode"]}}, i["id"])

    stops = None
    offer = None
    res = None
    print(f"Searching flights to {i['city']}...")

    try:
        today = datetime.now()
        departure = today + timedelta(days=1)
        return_d = departure + timedelta(days=180)

        params = {
            "originLocationCode": "LON",
            "destinationLocationCode": i["iataCode"],
            "departureDate": departure.strftime("%Y-%m-%d"),
            "returnDate": return_d.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "GBP",
            "max": 3,
            "nonStop": "true"
        }

        response = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers",
                                headers=headers, params=params)

        # If no direct flight, try with stops
        if not response.json().get("data"):
            params["nonStop"] = "false"
            response = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers",
                                    headers=headers, params=params)

            segments = response.json()["data"][0]["itineraries"][0]["segments"]
            stops = len(segments)
            body = ""
            p = inflect.engine()

            for n in range(stops):
                departure_code = segments[n]["departure"]["iataCode"]
                arrival_code = segments[n]["arrival"]["iataCode"]
                departure_time = parse(segments[n]["departure"]["at"]).strftime("%d %b %Y on %H:%M")
                arrival_time = parse(segments[n]["arrival"]["at"]).strftime("%d %b %Y on %H:%M")

                body += (
                    f"The {p.ordinal(n + 1)} stop is from {departure_code} to {arrival_code}. "
                    f"Departure at: {departure_time}, Arrival at: {arrival_time}\n\n"
                )

        data_json = response.json()

        if "data" in data_json and data_json["data"]:
            offer = float(data_json["data"][0]["price"]["total"])
            res = data_json["data"][0]

    except Exception as e:
        print(f"❌ Error fetching data for {i['city']}: {e}")
        continue

    # Check price and notify
    sheet_price = i["lowestPrice"]
    if offer is not None and offer < sheet_price:
        try:
            dep_segment = res["itineraries"][0]["segments"][0]
            dep = parse(dep_segment["departure"]["at"]).strftime("%d %b %Y at %H:%M")

            try:
                ret_segment = res["itineraries"][1]["segments"][-1]
                ret = parse(ret_segment["arrival"]["at"]).strftime("%d %b %Y at %H:%M")
            except IndexError:
                ret = "N/A"

            notifier.notify(
                price=offer,
                your_city="London",
                destination=i["city"],
                takeoff=dep,
                return_date=ret,
                emails=data.emails
            )

            if stops is not None:
                notifier.indirect_flight(body=body, emails=data.emails)

        except Exception as e:
            print(f"⚠️ Error during notification for {i['city']}: {e}")

    print(f"{i['city']}: £{offer if offer else 'No flights'}")
    time.sleep(0.5)
