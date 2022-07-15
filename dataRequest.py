import createGraph

import pandas as pd
import requests

token = 'XQaHgOfNlBGkEDhohjTElRwVcMwmbjIc'

url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
datasetid = 'datasetid=GHCND'

limit = 'limit=1000'
units = 'units=metric'
offset = 'offset=0'

def buildURL(startdate, enddate, station, datatype):
	u = url + '?' + datasetid + '&' + datatype + '&stationid=GHCND:' + station + '&' + startdate + '&' + enddate + '&' + limit + '&' + units + '&' + offset
	return u

def buildListForDate(year, station, debug):
	if debug:
		print('Start buildDataframeForDate function')

	# datatype: TMIN, TMAX, PRCP, or SNOW
	tmin = requestData(year, station, 'TMIN', debug)
	tmax = requestData(year, station, 'TMAX', debug)
	prcp = requestData(year, station, 'PRCP', debug)
	snow = requestData(year, station, 'SNOW', debug)
	if debug:
		print('tmin.columns: ')
		print(tmin.columns)

		print('tmax.columns: ')
		print(tmax.columns)

		print('prcp.columns: ')
		print(prcp.columns)

		print('snow.columns: ')
		print(snow.columns)

	tmin = tmin.rename(columns = {'value' : 'TMIN'})
	tmax = tmax.rename(columns = {'value' : 'TMAX'})
	prcp = prcp.rename(columns = {'value' : 'PRCP'})
	snow = snow.rename(columns = {'value' : 'SNOW'})
	if debug:
		print('tmin.columns: ')
		print(tmin.columns)

		print('tmax.columns: ')
		print(tmax.columns)

		print('prcp.columns: ')
		print(prcp.columns)

		print('snow.columns: ')
		print(snow.columns)

	output = {
		'tmax' : [],
		'tmin' : [],
		'avgtemp' : [],
		'prcp' : [],
		'snow' : []
	}

	output['tmax'] = list(tmin['TMIN'])
	output['tmin'] = list(tmax['TMAX'])
	output['avgtemp'] = list((tmin['TMIN'] + tmax['TMAX']) / 2)
	output['prcp'] = list(prcp['PRCP'])
	output['snow'] = list(snow['SNOW'])
	if debug:
		print(output)
		print('End buildDataframeForDate function')

	return output

def requestData(year, station, datatype, debug):
	if debug:
		print('Start requestData function')

	startdate = 'startdate=' + str(year) + '-01-01'
	enddate = 'enddate=' + str(year) + '-12-31'

	url = buildURL(startdate, enddate, station, 'datatypeid=' + datatype)
	if debug:
		print('url: ')
		print(url)

	df = pd.DataFrame(requests.get(url, headers={'token': token}).json()["results"])
	df = df.drop(columns=['datatype', 'station', 'attributes'])
	if debug:
		print('df: ')
		print(df)

	if debug:
		print('End requestData function')

	return df