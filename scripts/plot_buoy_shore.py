#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt

degree_sign= u'\N{DEGREE SIGN}'

# Set font for matplotlib figures
#pyplot.rc('font', **{'size': 30})
# pyplot.rc('legend', **{'fontsize': 24})
# pyplot.rc('axes', **{'labelsize': 24})
# pyplot.rc('xtick', **{'labelsize': 24})
# pyplot.rc('ytick', **{'labelsize': 24})

# legend_location = 'upper center'
# legend_bbox_to_anchor = (0.5, -0.12)
#
# legend_location0='center right'
# legend_bbox_to_anchor0=(1.1, 0.5)


CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/buoy_boathouse_odo_sat.csv"


with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))


data_week_8 = your_list[1:142,0]
data_week_8 = data_week_8.astype('float32')
steps = 192.0 / data_week_8.size
points_week_8 = np.arange(0.0, 191.0, steps)

data_week_9 = your_list[1:193,1]
data_week_9 = data_week_9.astype('float32')
steps = 192.0 / data_week_9.size
points_week_9 = np.arange(0.0, 192.0, steps)

data_week_10 = your_list[1:179,2]
data_week_10 = data_week_10.astype('float32')
steps = 192.0 / data_week_10.size
points_week_10 = np.arange(0.0, 192.0, steps)

data_week_11 = your_list[1:171,3]
data_week_11 = data_week_11.astype('float32')
steps = 192.0 / data_week_11.size
points_week_11 = np.arange(0.0, 192.0, steps)

fig, ax1 = plt.subplots()

# ax1.set_title('Mini-Buoy to Shore: Temperature (' + degree_sign + 'C)')
ax1.set_title('Mini-Buoy to Shore: Dissolved Oxygen (%sat)')

color_week_8 = '#ff6db6'
color_week_9 = '#24ff24'
color_week_10 = '#ffff6d'
color_week_11 = '#000000'

# ax1.set_ylabel('Temperature (' + degree_sign + 'C)')
ax1.set_ylabel('Dissolved Oxygen (%sat)')
ax1.plot(points_week_8, data_week_8, color=color_week_8)
ax1.plot(points_week_9, data_week_9, color=color_week_9)
ax1.plot(points_week_10, data_week_10, color=color_week_10)
ax1.plot(points_week_11, data_week_11, color=color_week_11)

loc = 'upper right'
ax1.legend(['Week 8', 'Week 9', 'Week 10', 'Week 11'], loc='upper right', bbox_to_anchor=(0.95, 0.85))

ax1.tick_params(axis='y')
# ax1.set_yticks(np.arange(6.0, 11.5, 0.5))
ax1.set_yticks(np.arange(92.0, 99.5, 0.5))

ax1.set_xticks(np.arange(0.0, 192.0, 191.0))
fig.canvas.draw()
ax1.set_xticklabels(['mini-buoy', 'shore'])

# ax2 = ax1.twinx()

# color = 'tab:blue'
# ax2.set_ylabel('Depth (m)', color=color)
# ax2.plot(sonde_time, sonde_depth, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# ax2.set_yticks(np.arange(0.0, 8.0, 0.5))


# fig.tight_layout()
plt.show()
