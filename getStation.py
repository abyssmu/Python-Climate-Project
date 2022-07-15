import pandas as pd
import pgeocode as geo

def getStationsFromZipcode(zipcode, debug):
	if debug:
		print('Start getStationsFromZipcode function')

	stations = pd.read_csv('stations.csv')
	if debug:
		print('stations: ')
		print(stations)

		print('stations.columns: ')
		print(stations.columns)

	locationInfo = geo.Nominatim('us').query_postal_code(zipcode)
	if debug:
		print('locationInfo: ')
		print(locationInfo)

	coordRange = 0.1

	substations = stations.loc[stations['state'] == locationInfo.state_code]

	substations = substations.loc[substations['lat'] < locationInfo.latitude + coordRange]
	substations = substations.loc[substations['lat'] > locationInfo.latitude - coordRange]

	substations = substations.loc[substations['lon'] < -locationInfo.longitude + coordRange]
	substations = substations.loc[substations['lon'] > -locationInfo.longitude - coordRange]

	substations = substations.loc[substations['id'].str.contains('USC')]

	if debug:
		print('substations: ')
		print(substations)
		print('End getStationsFromZipcode function')

	return substations