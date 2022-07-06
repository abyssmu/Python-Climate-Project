import dataRequest
import getStation

import pandas as pd
import matplotlib.pyplot as plt

# startDate = 2000
# endDate = 2019

# dR.requestBasics(startDate, endDate, 'data')

debug = False

stations = getStation.getStationsFromZipcode('61801', debug)

if debug:
	print(stations)

startYear = 2000
endYear = 2002

# datatype: TMIN, TMAX, or SNOW
datatype = 'TMIN'

df = dataRequest.requestRange(startYear, endYear, datatype, debug)
print(df.columns)

df = df.rename(columns = {'value' : datatype})
print(df.columns)

df.plot()
plt.show()