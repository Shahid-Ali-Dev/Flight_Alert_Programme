# ✈️ Flight Alert

**Flight Alert** is a Python-based airfare tracking tool that monitors flight prices for multiple destinations and sends you instant notifications when it finds a cheaper deal than your set budget.  
It integrates with the **Amadeus Flight API** to search for flights and supports both direct and indirect routes.

---

## 📌 Features

- **Automated Flight Search** – Continuously checks prices for your saved destinations.
- **Direct & Indirect Flight Detection** – Falls back to flights with stopovers if no direct ones are available.
- **Custom Price Thresholds** – Set your own maximum price for each destination.
- **Email Notifications** – Get notified instantly when a deal is found.
- **IATA Code Auto-Fetch** – Automatically retrieves missing airport codes.
- **Multi-Destination Support** – Track multiple locations in one run.

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **APIs**:  
  - [Amadeus API](https://developers.amadeus.com/) for flight search  
- **Libraries**:
  - `requests` – API calls
  - `dateutil` – Parsing flight dates
  - `inflect` – Ordinal formatting for stopovers
  - `time`, `datetime` – Scheduling checks

---

## 👨‍💻Programme Structure

flight-alert/
- │
- ├── main.py # Main program logic
- ├── data_manager.py # Reads/writes data to Google Sheets or local storage
- ├── flight_search.py # Handles API calls to search for flights
- ├── notification_manager.py # Sends email alerts
- ├── requirements.txt # Required dependencies
- └── README.md # Project documentation

---

## .env Structure
-Authorization_offers=           # Authorization token for offers API (if required by service)
-amend_api_key=                   # Amadeus API key for flight search
-amend_secret=                    # Amadeus API secret for authentication
-account_sid=                     # Twilio Account SID for sending SMS alerts
-auth_token=                      # Twilio Auth Token for SMS authentication
-base_sheety_url=                 # Sheety API endpoint for Google Sheets data
-api_key=                         # General API key for any additional flight APIs
-smtp_email=                      # Email address used for sending notifications
-smtp_password=                   # App-specific password for SMTP email service
-twilio_from=                     # Twilio phone number to send SMS from
-twilio_to=                       # Destination phone number to send SMS to

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flight-alert.git
   cd flight-alert
