import requests


class FlightSearch:

    def __init__(self):
        self.key = "key"
        self.headers = {"apikey": self.key}
        self.iata_url = "https://api.tequila.kiwi.com/locations/query"
        self.search_url = "https://api.tequila.kiwi.com/v2/search"

    def search(self, from_date, to_date, from_city, to_city):
        search_parameters = {"fly_from": f"city:{from_city}", "fly_to": f"city:{to_city}", "dateFrom": f"{from_date}", "dateTo": f"{to_date}", "curr": "USD"}
        response = requests.get(url=self.search_url, headers=self.headers, params=search_parameters)
        response.raise_for_status()
        response = response.json()
        return [response["data"][i]["price"] for i in range(len(response["data"]))]

    def get_iata_code(self, city_name):
        iata_parameters = {"term": f"{city_name}", "location_types": "city"}
        response = requests.get(url=self.iata_url, headers=self.headers, params=iata_parameters)
        response.raise_for_status()
        response = response.json()
        return response["locations"][0]["code"]