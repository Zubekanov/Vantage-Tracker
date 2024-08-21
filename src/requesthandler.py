import requests
import os

class RequestHandler:
    def __init__(self):
        pass

class Request:
    args: dict
    url: str
    method: str
    response: requests.Response = None

    def __init__(self, method: str, url:str, args: dict = {}):
        self.args = args
        self.url = url
        self.method = method

    def make_request(self):
        request_url = self.build_request()
        response: requests.Response

        match self.method:
            case "get":
                response = requests.get(request_url)
            case "post":
                response = requests.post(request_url)
            case "put":
                response = requests.put(request_url)
            case "delete":
                response = requests.delete(request_url)
            case _:
                raise Exception(f"Invalid method \"{self.method}\" passed.")
        
        self.response = response
    
    def build_request(self):
        request_url = self.url

        if len(self.args.keys()) > 0:
            request_url += "?"
        else:
            return request_url
        
        for key, value in self.args.items():
            request_url += key + "=" + value + "&"

        return request_url[:-1]
    
    def get_response(self):
        return self.response