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
