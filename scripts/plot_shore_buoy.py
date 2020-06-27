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


CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/boathouse_buoy_temp.csv"


with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))


# data_week_n4 = your_list[1:168,0]
# data_week_n4 = data_week_n4.astype('float32')
# steps = 396.0 / data_week_n4.size
# points_week_n4 = np.arange(0.0, 396.0, steps)
#
# data_week_n3 = your_list[1:104,1]
# data_week_n3 = data_week_n3.astype('float32')
# steps = 396.0 / data_week_n3.size
# points_week_n3 = np.arange(0.0, 396.0, steps)
#
# data_week_n2 = your_list[1:114,2]
# data_week_n2 = data_week_n2.astype('float32')
# steps = 396.0 / data_week_n2.size
# points_week_n2 = np.arange(0.0, 396.0, steps)
#
# data_week_n1 = your_list[1:169,3]
# data_week_n1 = data_week_n1.astype('float32')
# steps = 396.0 / data_week_n1.size
# points_week_n1 = np.arange(0.0, 396.0, steps)

# data_week_0 = your_list[1:200,4]
# data_week_0 = data_week_0.astype('float32')
# steps = 396.0 / data_week_0.size
# points_week_0 = np.arange(0.0, 396.0, steps)

data_week_1 = your_list[1:381,5]
data_week_1 = data_week_1.astype('float32')
steps = 396.0 / data_week_1.size
points_week_1 = np.arange(0.0, 395.0, steps)

data_week_2 = your_list[1:377,6]
data_week_2 = data_week_2.astype('float32')
steps = 396.0 / data_week_2.size
points_week_2 = np.arange(0.0, 395.0, steps)

data_week_3 = your_list[1:371,7]
data_week_3 = data_week_3.astype('float32')
steps = 396.0 / data_week_3.size
points_week_3 = np.arange(0.0, 396.0, steps)

data_week_4 = your_list[1:202,8]
data_week_4 = data_week_4.astype('float32')
steps = 396.0 / data_week_4.size
points_week_4 = np.arange(0.0, 396.0, steps)

data_week_5 = your_list[1:330,9]
data_week_5 = data_week_5.astype('float32')
steps = 396.0 / data_week_5.size
points_week_5 = np.arange(0.0, 396.0, steps)

data_week_6 = your_list[1:396,10]
data_week_6 = data_week_6.astype('float32')
steps = 396.0 / data_week_6.size
points_week_6 = np.arange(0.0, 396.0, steps)

fig, ax1 = plt.subplots()

ax1.set_title('Shore to Mini-Buoy: Temperature (' + degree_sign + 'C)')
# ax1.set_title('Shore to Mini-Buoy: Dissolved Oxygen (%sat)')

color_week_n4 = '#924900'
color_week_n3 = '#009292'
color_week_n2 = '#ffb6db'
color_week_n1 = '#006ddb'
color_week_0 = '#490049'
color_week_1 = '#920000'
color_week_2 = '#db6d00'
color_week_3 = '#ff6db6'
color_week_4 = '#24ff24'
color_week_5 = '#ffff6d'
color_week_6 = '#000000'

ax1.set_ylabel('Temperature (' + degree_sign + 'C)')
# ax1.set_ylabel('Dissolved Oxygen (%sat)')
# ax1.plot(points_week_n4, data_week_n4, color=color_week_n4)
# ax1.plot(points_week_n3, data_week_n3, color=color_week_n3)
# ax1.plot(points_week_n2, data_week_n2, color=color_week_n2)
# ax1.plot(points_week_n1, data_week_n1, color=color_week_n1)
# ax1.plot(points_week_0, data_week_0, color=color_week_0)
ax1.plot(points_week_1, data_week_1, color=color_week_1)
ax1.plot(points_week_2, data_week_2, color=color_week_2)
ax1.plot(points_week_3, data_week_3, color=color_week_3)
ax1.plot(points_week_4, data_week_4, color=color_week_4)
ax1.plot(points_week_5, data_week_5, color=color_week_5)
ax1.plot(points_week_6, data_week_6, color=color_week_6)

loc = 'upper right'
# ax1.legend(['Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11'], loc='upper right', bbox_to_anchor=(0.95, 0.85)
ax1.legend(['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'], loc='upper right')

ax1.tick_params(axis='y')
ax1.set_yticks(np.arange(4.5, 11.5, 0.5))
# ax1.set_yticks(np.arange(91.0, 99.0, 1.0))

ax1.set_xticks(np.arange(0.0, 396.0, 395.0))
fig.canvas.draw()
ax1.set_xticklabels(['shore', 'mini-buoy'])

# ax2 = ax1.twinx()

# color = 'tab:blue'
# ax2.set_ylabel('Depth (m)', color=color)
# ax2.plot(sonde_time, sonde_depth, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# ax2.set_yticks(np.arange(0.0, 8.0, 0.5))


# fig.tight_layout()
plt.show()
