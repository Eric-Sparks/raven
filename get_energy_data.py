#!/usr/bin/python3
import json
import requests
import pprint

api_url_base = 'http://192.168.1.214/api/meters/aggregates'

r = requests.get(url=api_url_base)
data = r.json()
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(data)
# An example of pulling out individual values
print("Solar power: ",data['solar']['instant_power'])
print("House load: ",data['load']['instant_power'])
print("Powerwall: ",data['battery']['instant_power'])
print("BGE: ",data['site']['instant_power'])

