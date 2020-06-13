import requests
from pprint import pprint

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {"path": "123.text"}
headers = {"Authorization:OAuth oauth_token=token, oauth_client_id=id"}


id = "ID: 792e5dcaf75a454f9dc7f53f653dd3ba"
Password = "0c34f27992aa459fbc013aeaa"
Callback_URL = "https://oauth.yandex.ru/verification_code"

token = "AgAAAAAKV4gXAAZkw3TOttBuzkMPkC8"

response = requests.put(url, headers=headers, params=params)

pprint(response.json())
