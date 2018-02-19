import config
import time
import requests
import json

today = time.strftime("%Y-%m-%d")

# define functions for handling news data
# News API - https://newsapi.org

def news_collection(tickers):
    for ticker in tickers:
        news_url = 'https://newsapi.org/v2/everything?q={0}&from={1}&apiKey={2}'.format(ticker, today, config.na_api_key)
        r = requests.get(news_url)
        print(json.dumps(r.json(), sort_keys=True, indent=4))
