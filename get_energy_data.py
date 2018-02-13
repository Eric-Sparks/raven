#!/usr/bin/python3
import json
import requests
import pprint
import pymysql.cursors

api_url_base = 'http://192.168.1.214/api/meters/aggregates'

r = requests.get(url=api_url_base)
data = r.json()
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(data)
# An example of pulling out individual values
#print("Solar power: ",data['solar']['instant_power'])
#print("House load: ",data['load']['instant_power'])
#print("Powerwall: ",data['battery']['instant_power'])
#print("BGE: ",data['site']['instant_power'])

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
        cursor.execute(sql,(data['battery']['energy_imported'], data['battery']['energy_exported'],\
        data['load']['instant_power'], data['load']['energy_imported'], data['load']['energy_exported'], \
        data['solar']['instant_power'], data['solar']['energy_imported'], data['solar']['energy_exported'], \
        data['site']['instant_power'], data['site']['energy_imported'], data['site']['energy_exported']))

finally:
# disconnect from server
    connection.close()

