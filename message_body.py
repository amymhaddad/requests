import requests

#Using POST to post new data using a dictionary:
url = "https://httpbin.org/post"
#First, set up the dict syntax with key, value. Then, add your data in the key, value format
response = requests.post(url, data={'key': 'value', 'brand': 'Ford', 'year': '2007'})

#Status code: check to make sure request was a success: response.status_code
#Headers: see headers of request  print(response.headers)

#Turn the response into a JSON-type object
json_response = response.json()

# print(json_response)
# >>>
# {'args': {}, 'data': '', 'files': {}, 'form': {'brand': 'Ford', 'key': 'value', 'year': '2007'}, 'headers': {'Accept':....
# Data goes into message body as a form ---> 'form': {'brand': 'Ford', 'key': 'value', 'year': '2007'}

print(json_response['headers']['Content-Type'])


#Using PSOT to post new data using a list of tuples
url = "https://httpbin.org/post"
response = requests.post(url, data=[('key', 'value'), ('brand', 'Ford'), ('year', '2007')])
#Check status of request: print(response.status_code)

#Turn repsonse into a JSON object 
json_response = response.json()
print(json_response['headers']['Content-Type'])

# Send POST data as JSON
url = "https://httpbin.org/post"
response = requests.post(url, json={'key': 'value', 'brand': 'Ford', 'year': '2007'})
#Check status: print(response.status_code)

#Look at the data
json_response = response.json()

print(json_response['headers']['Content-Type'])
# >>>
# application/json ---> The data was converted into json