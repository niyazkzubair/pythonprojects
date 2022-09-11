import requests

# set up the request parameters
params = {
  'api_key': 'A22808CF32534A63B61500F17FCFFDC4',
  'location': 'New York,New York,United States',
  'q': 'bitcoin'
}

# make the http GET request to Scale SERP
api_result = requests.get('https://api.scaleserp.com/search', params)

# print the JSON response from Scale SERP
print(json.dumps(api_result.json()))