## Synopsis

This project is an exercise in data visualization with Python. The objective is to retrieve financial data for a number of publicly traded companies and to graph relevant data related to stock performance.

## Requirements

* import time
* import requests
* import io
* import json
* import numpy as np
* import pandas as pd

This script also requires an API key for **AlphaVantage** as well as an API key for **newsapi.org**. Due to the sensitive nature of API keys, I have obfuscated mine. I intend to provide a demo version of this script in a future update, to allow visitors to my Github page to see the script in action.

## Lessons Learned

* Retrieving and storing JSON data from multiple APIs based on a single variable
* Parsing through and extracting subsets of JSON data
* Python classes

## To-do list

* Accept user input for ticker symbols
* Clean data for display
* Organize data logically
* Create charts
    * Simultaneously chart two tickers for comparison
