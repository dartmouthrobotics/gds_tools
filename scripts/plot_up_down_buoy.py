#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt

degree_sign= u'\N{DEGREE SIGN}'


CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/up_down_buoy_odo_sat.csv"
CSV_FILE_PATH_2 = "/home/darobot/Research/water_quality/src/gds_tools/data/up_down_buoy_depth.csv"


with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))

with open(CSV_FILE_PATH_2, 'r') as csv_file:
    reader = csv.reader(csv_file)
    depth_list = np.array(list(reader))


data_week_1 = your_list[1:128,0]
data_week_1 = data_week_1.astype('float32')
depth_week_1 = depth_list[1:128,0]
depth_week_1 = depth_week_1.astype('float32')

data_week_2 = your_list[1:201,1]
data_week_2 = data_week_2.astype('float32')
depth_week_2 = depth_list[1:201,1]
depth_week_2 = depth_week_2.astype('float32')

data_week_3 = your_list[1:754,2]
data_week_3 = data_week_3.astype('float32')
depth_week_3 = depth_list[1:754,2]
depth_week_3 = depth_week_3.astype('float32')

data_week_4 = your_list[1:913,3]
data_week_4 = data_week_4.astype('float32')
depth_week_4 = depth_list[1:913,3]
depth_week_4 = depth_week_4.astype('float32')

data_week_5 = your_list[1:774,4]
data_week_5 = data_week_5.astype('float32')
depth_week_5 = depth_list[1:774,4]
depth_week_5 = depth_week_5.astype('float32')

data_week_6 = your_list[1:907,5]
data_week_6 = data_week_6.astype('float32')
depth_week_6 = depth_list[1:907,5]
depth_week_6 = depth_week_6.astype('float32')

fig, ax1 = plt.subplots()

# ax1.set_title('ROV at Mini-Buoy: Temperature (' + degree_sign + 'C)')
ax1.set_title('ROV at Mini-Buoy: Dissolved Oxygen (%sat)')

color_week_1 = '#920000'
color_week_2 = '#db6d00'
color_week_3 = '#ff6db6'
color_week_4 = '#24ff24'
color_week_5 = '#ffff6d'
color_week_6 = '#000000'

# ax1.set_xlabel('Temperature (' + degree_sign + 'C)')
ax1.set_xlabel('Dissolved Oxygen (%sat)')
ax1.set_ylabel('Depth (m)')

ax1.scatter(data_week_1, depth_week_1, color=color_week_1)
ax1.scatter(data_week_2, depth_week_2, color=color_week_2)
ax1.scatter(data_week_3, depth_week_3, color=color_week_3)
ax1.scatter(data_week_4, depth_week_4, color=color_week_4)
ax1.scatter(data_week_5, depth_week_5, color=color_week_5)
ax1.scatter(data_week_6, depth_week_6, color=color_week_6)

loc = 'upper right'
# ax1.legend(['Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11'], loc='upper right', bbox_to_anchor=(0.95, 0.85)
ax1.legend(['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'], loc='lower right')

# ax1.tick_params(axis='y')
# ax1.set_xticks(np.arange(4.5, 11.5, 0.5))
ax1.set_xticks(np.arange(91.5, 100.0, 1.0))
ax1.set_yticks(np.arange(8.0, -0.5, -0.5))
plt.gca().invert_yaxis()

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
