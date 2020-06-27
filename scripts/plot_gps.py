#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.tri as tri
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
from matplotlib import ticker, cm
import numpy as np
from numpy import ma
import csv

degree_sign= u'\N{DEGREE SIGN}'

CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/catabot_exploration_temp.csv"
CSV_FILE_PATH_2 = "/home/darobot/Research/water_quality/src/gds_tools/data/catabot_exploration_gps.csv"

with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))

with open(CSV_FILE_PATH_2, 'r') as csv_file:
    reader = csv.reader(csv_file)
    gps_list = np.array(list(reader))

# week 3
# z = your_list[1:1323,2]
# z = z.astype('float32')
# week 5
# z = your_list[1:2394,1]
# z = z.astype('float32')
# week 6
# z = your_list[1:2839,0]
# z = z.astype('float32')
# week 6 part 2
z = your_list[1:2608,3]
z = z.astype('float32')

# week 3
# x = gps_list[1:1323,5]
# x = x.astype('float32')
# y = gps_list[1:1323,4]
# y = y.astype('float32')
# week 5
# x = gps_list[1:2394,3]
# x = x.astype('float32')
# y = gps_list[1:2394,2]
# y = y.astype('float32')
# week 6
# x = gps_list[1:2839,1]
# x = x.astype('float32')
# y = gps_list[1:2839,0]
# y = y.astype('float32')
# week 6 part 2
x = gps_list[1:2608,7]
x = x.astype('float32')
y = gps_list[1:2608,6]
y = y.astype('float32')

f, ax = plt.subplots()
ax.set_title('Catabot Week 6 Path 2: Temperature (' + degree_sign + 'C)')

cs = ax.tricontourf(x,y,z, 10, norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03,
                                              vmin=10.8, vmax=13.1))
# cs = ax.tricontourf(x,y,z, 10)

# cs.set_clim(vmin=6.5, vmax=13.0)
# bounds = np.arange(6.5, 13.5, 0.5)
# print(bounds)


f.colorbar(cs, orientation='horizontal', format='%.1f')


# cbar = f.colorbar(cs, vmin=6.0, vmax=13.5, boundaries=[6.0]+bounds+[13.5], extend='both', ticks=bounds)
# cbar.ax.set_yticklabels(['6.5', '7.0', '7.5', '8.0', '8.5', '9.0', '9.5', '10.0', '10.5', '11.0', '11.5', '12.0', '12.5', '13.0'])




# plt.xticks(np.arange(-72.0380, -72.0355, 0.0005))

ax.set_xlabel('Longitude')
plt.xlim([-72.0375, -72.0345])
ax.set_xticks(np.arange(-72.0375, -72.0344, 0.0005))
f.canvas.draw()
ax.set_xticklabels(['-72.0375', '-72.0370', '-72.0365', '-72.0360', '-72.0355', '-72.0350', '-72.0345'])

ax.set_ylabel('Latitude')
plt.ylim([43.4099, 43.4115])
ax.set_yticks(np.arange(43.4100, 43.4116, 0.0005))
f.canvas.draw()
ax.set_yticklabels(['43.4100', '43.4105', '43.4110', '43.4115'])


ax.plot(x,y,marker='o', color='k', markersize=0.1)
ax.set_aspect('equal')
plt.grid(True)

ax.plot(np.array([-72.0365116]), np.array([43.410345]), color='k', marker='o', markersize=13)
ax.plot(np.array([-72.0365116]), np.array([43.410345]), color='#FF4500', marker='o', markersize=8)

ax.plot(np.array([-72.0369625]), np.array([43.4100466]), color='k', marker=(5,1), markersize=16)
ax.plot(np.array([-72.0369625]), np.array([43.4100466]), color='#FF4500', marker=(5,1), markersize=8)

bar = AnchoredSizeBar(ax.transData, 0.00046, '40 m', 4)
ax.add_artist(bar)


plt.show()
