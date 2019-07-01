import requests

url = "https://httpbin.org/get"

response = requests.get(url)


# print(response.json)
# response.text
json_response = response.json() #This is a dict

#cycle through this dict to get key, val pairs. Then, I can drill down into the dict by indexing with a key
def print_d(json):
    for key, value in json.items():
        print(f"{key} : {value}")

# print(print_d(json_response))
#>>>
# args : {}
# headers : {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0'}
# origin : 66.30.209.98, 66.30.209.98
# url : https://httpbin.org/get

#Get specific info from the reponse --> index into response (which is a dict). Just index into the dict using the key (extracted from the json_response dict in function above)
# print(json_response['headers'])

#Look at response headers to get metadata 

print(print_d(response.headers))
#Print headers, which are case INSENSTIVE
#>>>
#Access-Control-Allow-Credentials : true
# Access-Control-Allow-Origin : *
# Content-Encoding : gzip
# Content-Type : application/json
# Date : Fri, 28 Jun 2019 14:29:37 GMT
# Referrer-Policy : no-referrer-when-downgrade
# Server : nginx
# X-Content-Type-Options : nosniff
# X-Frame-Options : DENY
# X-XSS-Protection : 1; mode=block
# Content-Length : 182
# Connection : keep-alive