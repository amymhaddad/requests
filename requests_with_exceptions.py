import requests
from requests.exceptions import HTTPError

for url in ["https://httpbin.org/get", "https://httpbin.org/get/demo"]:
    try:
        request = requests.get(url)
        request.raise_for_status()

    except HTTPError as http_err:
        print(f"An {http_err} error has occured")
    
    except Exception as err:
        print(f"An {err} has occured")
    
    else:
        print("success")