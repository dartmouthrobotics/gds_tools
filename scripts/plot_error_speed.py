#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt

degree_sign= u'\N{DEGREE SIGN}'

CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/bluerov2_sonde_2020-05-17-lake-sunapee-part-1.csv"
# CSV_FILE_PATH_2 = "/home/darobot/Research/water_quality/src/gds_tools/data/error_speed_up_down_buoy_depth.csv"


with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))

# with open(CSV_FILE_PATH_2, 'r') as csv_file:
#     reader = csv.reader(csv_file)
#     depth_list = np.array(list(reader))

# sonde_temp_up = your_list[1:1922,0]
# sonde_temp_up = sonde_temp_up.astype('float32')
# sonde_temp_down = your_list[1:1886,1]
# sonde_temp_down = sonde_temp_down.astype('float32')
#
# sonde_depth_up = depth_list[1:1922,0]
# sonde_depth_up = sonde_depth_up.astype('float32')
# sonde_depth_down = depth_list[1:1886,1]
# sonde_depth_down = sonde_depth_down.astype('float32')


sonde_temp = your_list[723:4530,36]
sonde_temp = sonde_temp.astype('float32')

sonde_depth = your_list[723:4530,22]
sonde_depth = sonde_depth.astype('float32')

sonde_time = np.arange(0,sonde_depth.size, 1)


fig, ax1 = plt.subplots()

ax1.set_title('ROV Vertical Movement: Temperature (' + degree_sign + 'C) and Depth (m)')

# ax1.set_xlabel('Temperature (' + degree_sign + 'C)')
# plt.xlim(8.3, 11.0)
#
# ax1.set_ylabel('Depth (m)')
# plt.gca().invert_yaxis()
#
# ax1.scatter(sonde_temp_up, sonde_depth_up, color='#920000', marker='o')
# ax1.scatter(sonde_temp_down, sonde_depth_down, color='#006ddb', marker='v')
# ax1.legend(['Upward', 'Downward'], loc='lower right')



color = 'tab:red'
ax1.set_xlabel('Time (s)')
# ax1.set_xlabel('Depth (m)')
# ax1.set_xticks(np.arange(0.0, 1000.0, 25))

ax1.set_ylabel('Temperature (' + degree_sign + 'C)', color=color)
ax1.plot(sonde_time, sonde_temp, color=color)
ax1.tick_params(axis='y', labelcolor=color)
# ax1.set_ylabel('Temperature (' + degree_sign + 'C)')
# ax1.scatter(sonde_depth, sonde_temp)
# ax1.set_yticks(np.arange(-0.6, 0.0, 0.1))

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Depth (m)', color=color)
ax2.plot(sonde_time, sonde_depth, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.gca().invert_yaxis()


# ax2.set_yticks(np.arange(0.0, 8.0, 0.5))



# fig.tight_layout()
plt.show()
