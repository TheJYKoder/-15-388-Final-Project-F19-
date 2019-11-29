import json
from matplotlib import pyplot as plt 
from matplotlib.ticker import MaxNLocator

years = [year for year in range(1999, 2019)]
rateCAD = []

for year in range(1999, 2019): 
	jsonData = open(str(year)+"-01-01.json", "r").read()
	data = json.loads(jsonData)
	rateCAD.append(data["rates"]["CHF"])

plt.xlabel("Year")
plt.ylabel("Canadian Dollar/US Dollar")
plt.plot(years,rateCAD)
plt.xticks(years)
plt.xticks(rotation=90)
plt.tick_params(axis='x', which='major', labelsize=7)
plt.show() 