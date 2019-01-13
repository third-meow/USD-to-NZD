import sys
import json
import requests

# read acess key from file
with open('secretkey.txt') as f:
    access_key = f.readline().strip()

# setup parametes dict
params = {
    'access_key': access_key,
    'currencies': 'USD,NZD',
}

# api call
res = requests.get('http://apilayer.net/api/live', params = params)

# save responce to file
with open('saved_exch_rate.json', 'w') as f:
    json.dump(res.json(), f)

# calculate exchange rate
exch_rate = float(res.json()['quotes']['USDNZD']);

# get amount
amount = float(sys.argv[-1])

# calc result
if "-r" in sys.argv:    # -r for converting NZD to USD
    result = amount / exch_rate
else:
    result = amount * exch_rate

# print result to 2dp
print(result - (result % 0.01))
