import requests, json
from requests.exceptions import HTTPError

url = "https://httpbin.org/get"
request = requests.get(url)

print(request.status_code)

# response = request.json()

#alt: response = json.loads(request.text)

# print(json.loads(request.text) == request.json())


# if response.status_code == 200:
#     print("success")
# elif response.status_code == 404:
#     print("fail")

# #alt:
# if response: #meaning: if response is True --> checking that the status code is in the range between 200-400, which is a successful status code. 
#     print("Success")
# else:
#     print("An error has occured")