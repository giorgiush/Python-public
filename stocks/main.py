import requests
import os


STOCKS_API_KEY = os.environ["STOCKS_API_KEY"]
parameters_stock = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": "IBM", "datatype": "compact", "apikey": STOCKS_API_KEY}


stocks = requests.get("https://www.alphavantage.co/query", params=parameters_stock)
stocks.raise_for_status()
stocks = stocks.json()
stocks_list = [i for i in stocks["Time Series (Daily)"]][:2]
YESTERDAY = float(stocks["Time Series (Daily)"][stocks_list[0]]["4. close"])
DAY_BEFORE_YESTERDAY = float(stocks["Time Series (Daily)"][stocks_list[1]]["4. close"])


if YESTERDAY > DAY_BEFORE_YESTERDAY:
    print("^")
else:
    print("v")


flactuation = abs(100 - (YESTERDAY*100/DAY_BEFORE_YESTERDAY))


if flactuation > 10:
    NEWS_API_KEY = os.environ["NEWS_API_KEY"]
    parameters_news = {"q": "IBM", "category": "technology", "apiKey": NEWS_API_KEY}
    news = requests.get("https://newsapi.org/v2/top-headlines", params=parameters_news)
    news.raise_for_status()
    news = news.json()
    print(news["articles"][0]["title"])

