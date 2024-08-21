from decouple import config
import requesthandler

vantage_url = "https://www.alphavantage.co/query"
vantage_args = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "HLI",
    "interval": "60min",
    "apikey": config("ALPHAVANTAGE_APIKEY")
}

request = requesthandler.Request("get", vantage_url, vantage_args)
request.make_request()
response = request.get_response()
print(response.json())