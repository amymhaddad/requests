import requests

#POST "posts" new content, so we add "post" to the path of the URL
url = "https://httpbin.org/post"

# post request -- send some form of data as a dictionary 
response = requests.post(url, data={'key':'value'})
json_repsonse = response.json()

#look at contents of response: status code, headers, body
print(response.status_code)
print(response.headers)
print(response.headers['Date'])

#To get the repsone BODY, convert it to a python dict: response.json() OR json.loads(response.text)
#THEN, call the dictionary and you can use the keys of the dictionary to index into the dict object

url = "https://httpbin.org/put"
response = requests.put(url, data={'key':'value'})
print(response.status_code)

url = "https://httpbin.org/delete"
response = requests.delete(url)
print(response.status_code)