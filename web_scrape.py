import requests

stock = "VNQ"

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function":"GLOBAL_QUOTE","symbol":stock}

headers = {
    'x-rapidapi-key': "90d24f17c2mshe7a5019d169744ep146773jsna039703c4990",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

result = response.json().get("Global Quote")
print(result['05. price'])