import datetime as d
import json
import os
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

	to_excel(df, fileName)

def to_excel(df, fileName):
	f = fileName + '.xlsx'

	if os.path.exists(f):
		os.remove(f)

	writer = pd.ExcelWriter(f, engine='xlsxwriter')

	r = len(df)
	for i in range(0, r):
		df[i].to_excel(writer, sheet_name=('Sheet' + str(i)))

	createChart(writer, r)

	writer.save()

def createChart(writer, r):
	for i in range(0, r):
		workbook = writer.book
		worksheet = writer.sheets['Sheet' + str(i)]

		chart = workbook.add_chart({'type': 'line'})

		chart.add_series({
			'categories': 'Sheet' + str(i) + '!$B$1:$B$366',
			'values': 'Sheet' + str(i) + '!$F$1:$F$366',})

		chart.set_x_axis({'name': 'Date', 'date_axis': True})
		chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': True}})
		chart.set_legend({'position': 'none'})
		chart.set_title({'name' : str(2000 + i)})

		worksheet.insert_chart('H1', chart)