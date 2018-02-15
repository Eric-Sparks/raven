# This script connects to the Telsa Powerwall 2 gateway API and shows
# the real-time electron between the solar panels, Powerwall, grid,
# and the house (load).
#
# This script uses the API instead of the querying the database to
# reduce the load on the database.  This script is set to update
# every 1 second or as defined in the time.sleep function.

#!/usr/bin/python3
import json
import requests
import pprint
import time

while True:

    api_url_base = 'http://192.168.1.214/api/meters/aggregates'

    r = requests.get(url=api_url_base)
    data = r.json()
    #pp = pprint.PrettyPrinter(indent=2)
    #pp.pprint(data)
    # An example of pulling out individual values
    print("Solar power: ",data['solar']['instant_power'])
    print("House load: ",data['load']['instant_power'])
    print("Powerwall: ",data['battery']['instant_power'])
    print("Grid: ",data['site']['instant_power'])
    
    time.sleep(1)

