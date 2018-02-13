import json
import requests

api_url_base = 'http://192.168.1.214/api/meters/aggregates'

r = requests.get(url=api_url_base)
print(r.json())
