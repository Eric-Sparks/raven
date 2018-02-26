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
# This script connects to the Telsa Powerwall 2 gateway API and records
# the real-time electron between the solar panels, Powerwall, grid,
# and the house (load).
#
# This script writes three data points from four sources (as noted
# above) to a MariaDB database. This script is set to update
# every 1 second or as defined in the time.sleep function.

#!/usr/bin/python3
import json
import requests
import pymysql.cursors
import time

while True:

    api_url_base = 'http://192.168.1.214/api/meters/aggregates'

    r = requests.get(url=api_url_base)
    data = r.json()

    # Insert this data into a db.

    # Open database connection
    connection = pymysql.connect(host='localhost',user='sol',password='TheSun',db='Energy_Usage',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Create new record
            sql = "INSERT INTO Gateway_Data(battery_instant_power, battery_energy_imported, battery_energy_exported, \
            load_instant_power, load_energy_imported, \
            solar_instant_power, solar_energy_imported, solar_energy_exported, \
            grid_instant_power, grid_energy_imported, grid_energy_exported) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

       # Execute the SQL command
            cursor.execute(sql,(data['battery']['instant_power'], data['battery']['energy_imported'], data['battery']['energy_exported'],\
            data['load']['instant_power'], data['load']['energy_imported'], \
            data['solar']['instant_power'], data['solar']['energy_imported'], data['solar']['energy_exported'], \
            data['site']['instant_power'], data['site']['energy_imported'], data['site']['energy_exported']))

        connection.commit()

    finally:
    # disconnect from server
        connection.close()

    time.sleep(1)

