import requests

url = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt"
r = requests.get(url, allow_redirects = True)

open('stations.txt', 'wb').write(r.content)

stations = pd.read_csv('stations.txt', sep = " ", header = None)
print(stations)

states = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE',
			'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
			'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT',
			'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK',
			'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT',
			'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY',
			'AB', 'BC', 'MB',
			'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

test = open('test.txt').readlines()
out = open('new.txt', 'w')

pos = 0

for i in range(len(test)):
	# if len(test[i]) > 3:
	# 	if test[i][pos] == " " and test[i][:2] in states:
	# 		test[i] = test[i][:pos] + ',' + test[i][pos + 1:]

	# 		print(test[i])
	
	test[i] = ',' + test[i]

	out.write(test[i])