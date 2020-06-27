#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt


CSV_FILE_PATH = "/home/darobot/Research/water_quality/src/gds_tools/data/error_crash_odo_sat.csv"
CSV_FILE_PATH_2 = "/home/darobot/Research/water_quality/src/gds_tools/data/error_crash_turbidity.csv"


with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    your_list = np.array(list(reader))

with open(CSV_FILE_PATH_2, 'r') as csv_file:
    reader = csv.reader(csv_file)
    turbidity_list = np.array(list(reader))

sonde_odo_sat = your_list[0:167,0]
sonde_odo_sat = sonde_odo_sat.astype('float32')

sonde_turbidity = turbidity_list[0:167,0]
sonde_turbidity = sonde_turbidity.astype('float32')

x_val = np.arange(0, 167, 1)
print(x_val.size)
print(sonde_odo_sat.size)


fig, ax1 = plt.subplots()

ax1.set_title('ROV Hits Sediment: Dissolved Oxygen (%sat) and Turbidity (FNU)')

color = 'tab:red'
ax1.set_xlabel('Time (s)')
# ax1.set_xlabel('Depth (m)')
# ax1.set_xticks(np.arange(0.0, 1000.0, 25))

ax1.set_ylabel('Dissolved Oxygen (%sat)', color=color)
ax1.plot(x_val, sonde_odo_sat, color=color)
ax1.tick_params(axis='y', labelcolor=color)
# ax1.set_ylabel('Temperature (' + degree_sign + 'C)')
# ax1.scatter(sonde_depth, sonde_temp)
# ax1.set_yticks(np.arange(-0.6, 0.0, 0.1))

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Turbidity (FNU)', color=color)
ax2.plot(x_val, sonde_turbidity, color=color)
ax2.tick_params(axis='y', labelcolor=color)
# ax2.set_yticks(np.arange(0.0, 8.0, 0.5))

plt.axvline(x=98, color='gray', linestyle='--')

# fig.tight_layout()
plt.show()
