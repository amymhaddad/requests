import requests, json

#search GH repos
repsonse = requests.get(
    "https://api.github.com/search/repositories",
    params={'q': 'requests+language:python'},
)

#inspect param attributes
json_response = repsonse.json()
# print(dir(json_response))
repository = json_response['items'][0]
print(f"Repo name {repository['name']}")
print(f"Repo description {repository['description']}")

# print('resonse', json_response)



# for key, value in json_response.items():
#     print(f"{key}: {value}")