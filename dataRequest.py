import pandas as pd
import requests

token = 'XQaHgOfNlBGkEDhohjTElRwVcMwmbjIc'

url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
datasetid = 'datasetid=GHCND'
stationid = 'stationid=GHCND:USC00118740'

limit = 'limit=1000'
units = 'units=metric'
offset = 'offset=0'

def buildURL(startdate, enddate, datatype):
	u = url + '?' + datasetid + '&' + datatype + '&' + stationid + '&' + startdate + '&' + enddate + '&' + limit + '&' + units + '&' + offset
	return u

def requestMaxTemp(startYear, endYear, fileName):
	datatypeid = 'datatypeid=TMAX'

	requestRange(startYear, endYear + 1, datatypeid, fileName)

def requestMinTemp(startYear, endYear, fileName):
	datatypeid = 'datatypeid=TMIN'

	requestRange(startYear, endYear + 1, datatypeid, fileName)

def requestSnow(startYear, endYear, fileName):
	datatypeid = 'datatypeid=SNOW'

	requestRange(startYear, endYear + 1, datatypeid, fileName)

def requestBasics(startYear, endYear, fileName):
	requestMaxTemp(startYear, endYear, fileName + 'TMAX')
	requestMinTemp(startYear, endYear, fileName + 'TMIN')
	requestSnow(startYear, endYear, fileName + 'SNOW')

def requestRange(startYear, endYear, datatype, fileName):
	tDiff = endYear - startYear
	df = tDiff*[None]

	for i in range(0, tDiff):
		year = startYear + i

		startdate = 'startdate=' + str(year) + '-01-01'
		enddate = 'enddate=' + str(year) + '-12-31'

		u = buildURL(startdate, enddate, datatype)

		df[i] = pd.DataFrame(requests.get(u, headers={'token': token}).json()["results"])