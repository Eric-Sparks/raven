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
            load_instant_power, load_energy_imported, load_energy_exported, \
            solar_instant_power, solar_energy_imported, solar_energy_exported, \
            grid_instant_power, grid_energy_imported, grid_energy_exported) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

       # Execute the SQL command
            cursor.execute(sql,(data['battery']['instant_power'], data['battery']['energy_imported'], data['battery']['energy_exported'],\
            data['load']['instant_power'], data['load']['energy_imported'], data['load']['energy_exported'], \
            data['solar']['instant_power'], data['solar']['energy_imported'], data['solar']['energy_exported'], \
            data['site']['instant_power'], data['site']['energy_imported'], data['site']['energy_exported']))

        connection.commit()

    finally:
    # disconnect from server
        connection.close()

    time.sleep(1)

