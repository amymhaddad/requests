import requests

response = requests.post("https://httpbin.org/post", json={'key': 'value'})
#Check the status of requst ---> print(response.status_code)

print(response.request.body)