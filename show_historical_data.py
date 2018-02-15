#!/usr/bin/python3
import json
import requests
import pymysql.cursors
import time

# Open database connection
connection = pymysql.connect(host='localhost',user='sol',password='TheSun',db='Energy_Usage',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
     # Compute amount of energy captured from solar panels.
     sql = "SELECT min(solar_energy_exported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     start_solar_odometer = cursor.fetchone()

     sql = "SELECT max(solar_energy_exported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     current_solar_odometer = cursor.fetchone()
     print("Energy captured by the solar panels: ")
     print((current_solar_odometer['max(solar_energy_exported)']) - (start_solar_odometer['min(solar_energy_exported)']))

     # Compute amount of energy used from the grid.
     sql = "SELECT min(grid_energy_imported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     start_solar_odometer = cursor.fetchone()

     sql = "SELECT max(grid_energy_imported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     current_solar_odometer = cursor.fetchone()
     print("Energy used from the grid: ")
     print((current_solar_odometer['max(grid_energy_imported)']) - (start_solar_odometer['min(grid_energy_imported)']))

     # Compute amount of energy sent to the grid.
     sql = "SELECT min(grid_energy_exported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     start_solar_odometer = cursor.fetchone()

     sql = "SELECT max(grid_energy_exported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     current_solar_odometer = cursor.fetchone()
     print("Energy sent to the grid: ")
     print((current_solar_odometer['max(grid_energy_exported)']) - (start_solar_odometer['min(grid_energy_exported)']))

     # Compute amount of energy sent to Powerwall
     sql = "SELECT min(battery_energy_imported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     start_solar_odometer = cursor.fetchone()

     sql = "SELECT max(battery_energy_imported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     current_solar_odometer = cursor.fetchone()
     print("Energy sent to Powerwall: ")
     print((current_solar_odometer['max(battery_energy_imported)']) - (start_solar_odometer['min(battery_energy_imported)']))

     # Compute amount of energy retrieved from Powerwall
     sql = "SELECT min(battery_energy_exported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     start_solar_odometer = cursor.fetchone()

     sql = "SELECT max(battery_energy_exported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     current_solar_odometer = cursor.fetchone()
     print("Energy retrieved from Powerwall: ")
     print((current_solar_odometer['max(battery_energy_exported)']) - (start_solar_odometer['min(battery_energy_exported)']))

     # Compute amount of energy used by the house
     sql = "SELECT min(load_energy_imported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     start_solar_odometer = cursor.fetchone()

     sql = "SELECT max(load_energy_imported) FROM `Gateway_Data` WHERE DATE(`date_time`) = CURDATE()"
     cursor.execute(sql)
     current_solar_odometer = cursor.fetchone()
     print("Energy used by the house: ")
     print((current_solar_odometer['max(load_energy_imported)']) - (start_solar_odometer['min(load_energy_imported)']))

finally:
     connection.close()
