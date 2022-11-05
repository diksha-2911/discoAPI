import requests

base_url = "https://api.stackexchange.com/"
path_url = "/2.3/similar?order=desc&sort=relevance&title={user message}&site=stackoverflow"

request_url = base_url + path_url

api_result = requests.get(request_url)
api_response = api_result.json()

for i in range(0, 5):
    print(api_response['items'][i]['link'])


