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


## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flight-alert.git
   cd flight-alert
