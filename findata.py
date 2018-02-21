# imports
import config
import time
import requests
import io
import json
import numpy as np
import pandas as pd

# define vars
print("What ticker symbol would you like to learn about?\n. . . . . \n")
sample_input = "MSFT"
tickers = [sample_input]
ticker_data = {}


class TickerFunctions():
    def stock_collection(self, ticker):
        self.ticker = ticker
        self.stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&datatype=csv&apikey={1}'.format(
            self.ticker, config.av_api_key)
        print('Fetching data for symbol {}...'.format(self.ticker))
        self.r = requests.get(self.stock_url).content
        self.stock_data = pd.read_csv(io.StringIO(self.r.decode('utf-8')))
        ticker_data[self.ticker] = pd.DataFrame(self.stock_data)

        # News collection handled by News API - https://newsapi.org

    def news_collection(self, ticker):
        self.today = time.strftime("%Y-%m-%d")
        self.news_url = 'https://newsapi.org/v2/everything?q={0}&from={1}&apiKey={2}'.format(
            self.ticker, self.today, config.na_api_key)
        self.r = requests.get(self.news_url)
        # print(json.dumps(self.r.json(), sort_keys=True, indent=4))

    def __init__(self, ticker):
        self.ticker = ticker
        self.stock_collection(self.ticker)
        self.news_collection(self.ticker)

    def data_overview(self, data):
        self.data = data
        for self.key in self.data.keys():
            print(self.key)
            print(self.data[self.key].head())
            print("-" * 75)
