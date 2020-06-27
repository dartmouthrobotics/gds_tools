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


CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/up_down_buoy_temp.csv"


with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))



data_week_6 = your_list[669:758,5]
data_week_6 = data_week_6.astype('float32')
steps = 89.0 / data_week_6.size
points_week_6 = np.arange(0.0, 89.0, steps)

fig, ax1 = plt.subplots()

# ax1.set_title('Shore to Mini-Buoy: Temperature (' + degree_sign + 'C)')
# ax1.set_title('Shore to Mini-Buoy: Dissolved Oxygen (%sat)')


color_week_6 = '#000000'

ax1.set_ylabel('Temperature (' + degree_sign + 'C)')
ax1.set_xlabel('Time (sec)')
# ax1.set_ylabel('Dissolved Oxygen (%sat)')

ax1.plot(points_week_6, data_week_6, color=color_week_6)

loc = 'upper right'
# ax1.legend(['Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11'], loc='upper right', bbox_to_anchor=(0.95, 0.85)
# ax1.legend(['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'], loc='upper right')

ax1.tick_params(axis='y')
ax1.set_yticks(np.arange(8.9, 9.2, 0.1))
# ax1.set_yticks(np.arange(94.5, 96.5, 0.5))

# ax1.set_xticks(np.arange(0.0, 396.0, 395.0))
# fig.canvas.draw()
# ax1.set_xticklabels(['shore', 'mini-buoy'])

# ax2 = ax1.twinx()

# color = 'tab:blue'
# ax2.set_ylabel('Depth (m)', color=color)
# ax2.plot(sonde_time, sonde_depth, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# ax2.set_yticks(np.arange(0.0, 8.0, 0.5))


# fig.tight_layout()
plt.show()
