import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Load our CSV file into a DataFrame
cities = pd.read_csv('california_cities.csv')
print(cities.info())

# Extract the data we're going to plot
lat = cities['latd'] # y values
lon = cities['longd'] # x values
pop = cities['population_total'] 
area = cities['area_total_sq_mi']

# Generate scatterplot 
plt.scatter(lon, lat, label=None, c=np.log10(pop), cmap='RdPu', s=area, linewidth=0, alpha=0.5)
# Customize & save figure
plt.axis('equal')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3,7)
plt.title('CA Cities: Area and Population')

# Customize the legend to show city's AREA
plt.ylabel('fLatitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3,7)
plt.title('CA Cities: Area and Population')

# Customize the legend to show city's AREA
# Plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([],[], c='k', alpha=0.3, s=area, label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1)


plt.savefig('cities.png')
