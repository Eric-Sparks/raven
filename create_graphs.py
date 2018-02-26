#    Raven imports energy usage, storage, and export data from Tesla Powerwall 2,
#    stores it, and offers to display it in a variety of formats.
#
#    Copyright (C) 2018 Eric H. Christensen
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
#   This script connects to the database, retrieves the requested data, and 
#   uses matplotlib to make graphs.
#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import pymysql.cursors
import requests

# Open database connection
connection = pymysql.connect(host='localhost',user='sol',password='TheSun',db='Energy_Usage',charset='utf8mb4',cursorclass=pymysql.cursors.SSCursor)

try:

    with connection.cursor() as cursor:
# Grab solar data for the last 7 days
        sql = "SELECT `date_time`,`solar_instant_power` FROM `Gateway_Data` WHERE DATE(`date_time`) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY_HOUR) and CURRENT_TIME() GROUP BY date_time ORDER BY date_time"
        cursor.execute(sql)
        weekly_solar = cursor.fetchall_unbuffered()

finally:
    connection.close

# Make the graph
fig, ax = plt.subplots()
ax.plot (weekly_solar)

ax.set(xlabel='Date', ylabel='Watts', title='Solar energy collected')
ax.grid()

fig.savefig("7_day_solar.png")
plt.show()

