from decouple import config
import requesthandler
import os

symbol_list = [
    "WDS",
    "HLI"
]

vantage_url = "https://www.alphavantage.co/query"
vantage_args = {
    "function": "TIME_SERIES_DAILY",
    "symbol": None,
    "outputsize": "full",
    "datatype": "json",
    "apikey": config("ALPHAVANTAGE_APIKEY")
}

requests_list = [
    {**vantage_args, "symbol": symbol} for symbol in symbol_list
]

for pos in range(len(symbol_list)):
    request = requesthandler.Request("get", vantage_url, requests_list[pos])
    request.make_request()
    response = request.get_response()

    if 200 >= response.status_code and response.status_code <= 300:
        file_path = os.path.join(os.path.dirname(__file__), ('data/daily_' + symbol_list[pos]))
        print("Writing historic data to daily_" + symbol_list[pos])
        file = open(file_path, "w")
        file.write(str(response.json()))
    else:
        print("Status code " + str(response.status_code) + " (" + str(response.reason) + ") recieved when requesting data for symbol " + symbol_list[pos])
