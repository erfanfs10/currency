import requests
import json
url = "https://api.apilayer.com/fixer/latest?base=USD"
cur = ["BTC", "USD", "IRR", "CAD", "AUD"]


def get_currency(api_key):
    payload = {}
    headers = {
        "apikey": api_key
    }

    total = []
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        res = json.loads(response.text)["rates"]
        for i in cur:
            total.append(res.get(i, "Not Found"))
        final = list(zip(cur, total))
    return final
