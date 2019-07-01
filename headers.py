import requests, json

#search GH repos
repsonse = requests.get(
    "https://api.github.com/search/repositories",
    #Have search look for "requests"
    params={'q': 'HTTP+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'}, #This is a GH text match media type AND we specify that it needs to be JSON (notice: '+json')
)

#Search through the response and return an list with where the search term appears
json_response = repsonse.json()
#Just get the first item
repository = json_response['items'][0]
#Return text matches, so look for that key
print(f"Text matches: {repository['text_matches']}")

Text matches: [{'object_url': 'https://api.github.com/repositories/1362490', 'object_type': 'Repository', 'property': 'description', 'fragment': 
'Python HTTP Requests for Humans™ ✨🍰✨', 'matches': [{'text': 'Requests', 'indices': [12, 20]}]}]
(.venv) 

>>>
[{'text': 'Requests', 'indices': [12, 20]}]}]
--->text match "Requests"   
--->indices give me a count to tell me where within the descirption ('Python HTTP Requests for Humans™') the word "requests" appears

Change the para to:  params={'q': 'HTTP+language:python'} and this is the result:
Text matches: [{'object_url': 'https://api.github.com/repositories/1362490', 'object_type': 'Repository', 
'property': 'description', 'fragment': 'Python HTTP Requests for Humans™ ✨🍰✨', 'matches': [{'text': 'HTTP', 'indices': [7, 11]}]}]
>>>
'HTTP' appears in the descirption at 7-11