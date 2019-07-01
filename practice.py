import requests, json

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# data = response.json()

#Question:
#Why increment by 1? Why can't I use a var to index into dict?


# user_dict = {}
# for user in data:
#     if user['completed']:
#         try:
#             # user_id = user['userId']
#             # user_dict['userID'] += 1
#             user_dict[user['userId']] += 1

#         except KeyError:
#              user_dict[user['userId']] =1

# print(user_dict)
    

#Question: extracting out of a dictionary
#I use dir(json_response) to see the methods and attributes I can use
#I want to use items --> json_response['items']  
#I'm trying to extract the "name" key from the dictionary and can't. why?

#search GH repos
# repsonse = requests.get(
#    "https://api.github.com/search/repositories",
#    params={'q': 'requests+language:python'},
# )

# # #inspect param attributes
# json_response = repsonse.json()

# for keys, value in json_response.items():
#     for key in keys:
#         print(json_response['items'])



# # print(type(json_response['items']))

# dict = {}
# for item in json_response:
#     if 'name':
#         print(dict[item['name']])
    



r = requests.put('https://httpbin.org/put', data = {'key':'value', 'q':'house'})

info = r.json()
print(info['headers']['Content-Type'])