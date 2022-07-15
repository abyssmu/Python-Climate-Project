import createGraph as cg
import dataRequest as dr
import getStation as gs

import matplotlib.pyplot as plt

debug = False
zipcode = '61801'

stations = gs.getStationsFromZipcode(zipcode, debug)

if debug:
	print(stations)

startYear = 1950
endYear = 1952

station = list(stations['id'])[0]
data = [dr.buildListForDate(startYear, station, debug)]

for i in range(1, endYear - startYear + 1):
	data.append(dr.buildListForDate(startYear + i, station, debug))

print(data)
cg.graphList(data, zipcode, startYear, debug)