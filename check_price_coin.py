import requests

def by_coin(prise):
    to = "phone_number"
    API_key = "your_API_key"
    url = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_key
    payload = {'receptor':to, 'message':'text_message'}
    response = requests.post(url, data=payload)
    print(response)
    
my_mony = 11000

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

# proxies = {
#   'http': "http://127.0.0.1:8118",
#   'https': "http://127.0.0.1:8118",
# }

response = requests.get(url)
prise = float(response.json()['data']['amount'])
print('at this moment, bitcoin is %i dollars' % prise)

if (prise < my_mony):
    by_coin(prise)
else:
    print('your mony is low')