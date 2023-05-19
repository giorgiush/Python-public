import requests
import flight_search
import datetime


date = datetime.datetime.now()
future = str(int(date.strftime("%m"))+1)
if len(future) == 1:
    future = f"0{future}"


class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/USER ID GOES HERE/flights/sheet1"
        self.headers = {"Authorization": f"Bearer token"}
        self.flight_search = flight_search.FlightSearch()
        self.today = date.strftime("%d/%m/%Y")
        self.future_date = date.strftime(f"%d/{future}/%Y")
        self.current_city = "OSA"

    def get_sheet_data(self):
        resp = requests.get(url=self.url, headers=self.headers)
        resp.raise_for_status()
        resp = resp.json()
        return resp

    def update_iata(self):
        for i in self.get_sheet_data()["sheet1"]:
            if not i["iataCode"]:
                url = f"https://api.sheety.co/USER ID GOES HERE/flights/sheet1/{i['id']}"
                params = {"sheet1": {"iataCode": self.flight_search.get_iata_code(i["city"])}}
                requests.put(url=url, headers=self.headers, json=params)

    def find_discount(self):
        for i in self.get_sheet_data()["sheet1"]:
            current_prices = self.flight_search.search(from_date=self.today, to_date=self.future_date, from_city=f"{self.current_city}", to_city=i["iataCode"])
            lowest_price = min(current_prices)
            if int(i["lowestPrice"]) > lowest_price:
                print(f"Flight to {i['city']} is ${lowest_price}")
            print(current_prices)




