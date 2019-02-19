import sys
import json
import requests
from requests.exceptions import ConnectionError

# read access key from file
with open('/home/third-meow/src/laptop/my_py/rand_tools/usd_to_nzd/secretkey.txt') as f:
    access_key = f.readline().strip()

# setup parametes dict
params = {
    'access_key': access_key,
    'currencies': 'USD,NZD',
}

try:
    # api call
    res = requests.get('http://apilayer.net/api/live', params=params).json()

    # save response to file
    with open('saved_exch_rate.json', 'w') as f:
        json.dump(res, f)

except ConnectionError:
    # open last saved response
    with open('saved_exch_rate.json', 'r') as f:
        res = json.load(f)

    # warn user
    print('Warning: cannot access latest exchange rate, using last saved rate')

# calculate exchange rate
exch_rate = float(res['quotes']['USDNZD'])

# get amount
amount = float(sys.argv[-1])

# calc result
if "-r" in sys.argv:    # -r for converting NZD to USD
    result = amount / exch_rate
else:
    result = amount * exch_rate

# print result to 2dp
print('{0:.2f}'.format(result))
