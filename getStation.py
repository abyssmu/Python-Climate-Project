import pandas as pd
import pgeocode as geo

def getStationsFromZipcode(zipcode, debug = False):
	print('Start getStationsFromZipcode function')

	stations = pd.read_csv('stations.csv')
	if debug:
		print(stations)
		print(stations.columns)

	locationInfo = geo.Nominatim('us').query_postal_code(zipcode)
	if debug:
		print(locationInfo)

	coordRange = 0.1

	substations = stations.loc[stations['state'] == locationInfo.state_code]

	substations = substations.loc[stations['lat'] < locationInfo.latitude + coordRange]
	substations = substations.loc[stations['lat'] > locationInfo.latitude - coordRange]

	substations = substations.loc[stations['lon'] < -locationInfo.longitude + coordRange]
	substations = substations.loc[stations['lon'] > -locationInfo.longitude - coordRange]

	if debug:
		print(substations)

	print('End getStationsFromZipcode function')

	return substations