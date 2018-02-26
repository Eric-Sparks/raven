#    Raven imports energy usage, storage, and export data from Tesla Powerwall 2,
#    stores it, and offers to display it in a variety of formats.
#
#    Copyright (C) 2018 Eric H. Christensen, Jared Smith
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
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

