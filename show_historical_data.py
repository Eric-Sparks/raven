#!/usr/bin/python3
import json
import requests
import pymysql.cursors
import time

# Open database connection
connection = pymysql.connect(host='localhost',user='sol',password='TheSun',db='Energy_Usage',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
     # Read starting solar number for the day.

     sql = "SELECT min(solar_energy_exported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     start_solar_odometer = cursor.fetchone()
     print(start_solar_odometer['min(solar_energy_exported)'])

finally:
     connection.close()
