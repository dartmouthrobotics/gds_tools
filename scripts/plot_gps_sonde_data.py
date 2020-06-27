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


CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/log_gps_depth_sonde_2020-03-19-lake-sunapee-part-1.csv"


with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))

sonde_time = your_list[395:1062,5]
sonde_time = sonde_time.astype('int32')
sonde_time = np.subtract(sonde_time, sonde_time[0])

sonde_depth = your_list[395:1062,10]
sonde_depth = sonde_depth.astype('float32')
sonde_depth = sonde_depth[:] * -1.0

sonde_chlorophyll = your_list[395:1062,8]
sonde_chlorophyll = sonde_chlorophyll.astype('float32')

sonde_odo_sat = your_list[395:1062,12]
sonde_odo_sat = sonde_odo_sat.astype('float32')

sonde_odo_local = your_list[395:1062,13]
sonde_odo_local = sonde_odo_local.astype('float32')

sonde_odo_mg_l = your_list[395:1062,14]
sonde_odo_mg_l = sonde_odo_mg_l.astype('float32')

sonde_temp = your_list[395:1062,24]
sonde_temp = sonde_temp.astype('float32')


fig, ax1 = plt.subplots()

ax1.set_title('Up and Down Buoy: Chlorophyll (RFU) and Depth (m)')

color = 'tab:red'
ax1.set_xlabel('Time (s)')
# ax1.set_xlabel('Depth (m)')
ax1.set_xticks(np.arange(0.0, 1000.0, 25))

ax1.set_ylabel('Chlorophyll (RFU)', color=color)
ax1.plot(sonde_time, sonde_chlorophyll, color=color)
ax1.tick_params(axis='y', labelcolor=color)
# ax1.set_ylabel('Temperature (' + degree_sign + 'C)')
# ax1.scatter(sonde_depth, sonde_temp)
# ax1.set_yticks(np.arange(-0.6, 0.0, 0.1))

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Depth (m)', color=color)
ax2.plot(sonde_time, sonde_depth, color=color)
ax2.tick_params(axis='y', labelcolor=color)
# ax2.set_yticks(np.arange(0.0, 8.0, 0.5))


# fig.tight_layout()
plt.show()
