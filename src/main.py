from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from pprint import pprint
import os
from dotenv import load_dotenv

# Load env vars from .env
load_dotenv()
token = os.environ.get("AV-API-TOKEN")

# Which stock do we want to look at?
stock = "AAPL"

'''
# Sample time series data retrieval
ts = TimeSeries(key=token, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='LOW',interval='1min', outputsize='full')
print(data.describe())
'''

# Sample fundamental data retrieval
fd = FundamentalData(key=token, output_format="pandas")

# Get income statement
income_stmts, _ = fd.get_income_statement_annual(symbol=stock)

# From the income statement, we want the most recent data years 
# Alpha Vantage only provides us with the 5 most recent years :(
val = income_stmts["fiscalDateEnding"]


print(income_stmts.head())