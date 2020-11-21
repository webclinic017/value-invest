from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import os
from dotenv import load_dotenv

# Load env vars from .env
load_dotenv()
token = os.environ.get("av-api-token")

ts = TimeSeries(key=token, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='LOW',interval='1min', outputsize='full')
pprint(data.head(2))
