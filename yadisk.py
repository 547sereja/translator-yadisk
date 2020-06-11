import requests
from pprint import pprint

url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {"path": "123.text"}
headers = {'Authizatio': 'OAuth AgAAAAAKV4gXAAZkw3TOttBuzkMPkC8wqmVrkUA'}

response = requests.put(url, headers=headers, params=params)

pprint(response.json())


















 # ? path=<путь, по которому следует загрузить файл>
 # & [overwrite=<признак перезаписи>]
 # & [fields=<свойства, которые нужно включить в ответ>]