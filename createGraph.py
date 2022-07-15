import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter as pw

def graphList(data, zipcode, startYear, debug):
	if debug:
		print('Start graphList function')
		print(data)
	
	fig = plt.figure()

	metadata = dict(title = 'Test', artist = 'Test')
	writer = pw(fps = 60, metadata = metadata)
	dpi = 100

	greyData = []
	year = startYear

	with writer.saving(fig, 'test.gif', dpi):
		for i in data:
			plt.clf()

			plt.title(str(zipcode) + ': ' + str(year))
			plt.xlabel('Day of the year')
			plt.ylabel('Temp (Celsius)')

			if greyData is not None:
				for j in greyData:
					plt.plot(j, linewidth = 0.5, c = str())

			for endpoint in list(range(0, len(i), 20)):
				plt.plot(i[:endpoint], 'r-', linewidth = 2.0)

				writer.grab_frame()

			greyData.append([])
			greyData[-1] = i.copy()

			year += 1

	if debug:
		print('End graphList function')