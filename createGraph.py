import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter as pw

def graphList(data, zipcode, startYear, debug):
	if debug:
		print('Start graphList function')
		print(data)
	
	fig, (ax1, ax2, ax3) = plt.subplots(3)

	metadata = dict(title = 'Test', artist = 'Test')
	writer = pw(fps = 60, metadata = metadata)
	dpi = 100

	greyData = []
	year = startYear

	with writer.saving(fig, 'test.gif', dpi):
		for i in data:
			ax1.clear()
			ax2.clear()
			ax3.clear()

			plt.suptitle(str(zipcode) + ': ' + str(year))
			plt.xlabel('Day of the year')

			ax1.set_ylabel('Avg Temp (Celsius)')			
			ax2.set_ylabel('Rainfall (mm)')
			ax3.set_ylabel('Snowfall (mm)')

			if greyData is not None:
				greyscale = 1
				for j in greyData:
					ax1.plot(j['avgtemp'], 'r-', linewidth = 0.5, c = str(0.8 / greyscale))
					ax2.plot(j['prcp'], 'b-', linewidth = 0.5, c = str(0.8 / greyscale))
					ax3.plot(j['snow'], 'c-', linewidth = 0.5, c = str(0.8 / greyscale))

					greyscale += 1

			for endpoint in list(range(0, len(i['avgtemp']), 20)):
				ax1.plot(i['avgtemp'][:endpoint], 'r-', linewidth = 2.0)
				ax2.plot(i['prcp'][:endpoint], 'b-', linewidth = 2.0)
				ax3.plot(i['snow'][:endpoint], 'c-', linewidth = 2.0)

				writer.grab_frame()

			greyData.append([])
			greyData[-1] = i.copy()

			year += 1

	if debug:
		print('End graphList function')