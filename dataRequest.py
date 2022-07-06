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

def requestRange(startYear, endYear, datatype, debug = False):
	tDiff = endYear - startYear	
	year = startYear

	startdate = 'startdate=' + str(year) + '-01-01'
	enddate = 'enddate=' + str(year) + '-12-31'

	u = buildURL(startdate, enddate, 'datatypeid=' + datatype)
	if debug:
		print(u)

	df = pd.DataFrame(requests.get(u, headers={'token': token}).json()["results"])
	if debug:
		print(u)

	return df