from scipy.io import loadmat, matlab
import numpy as np
import matplotlib.pyplot as plt
import csv

import module_locator

x_file = module_locator.module_path() + '/csv/step_stepdis_dataX.csv'
y_file = module_locator.module_path() + '/csv/step_stepdis_dataY.csv'




with open(x_file) as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='"')
    x = []
    for row in r:
        # print(row)
        for n in row:
            x.append(float(n))

    # print(x_data)

with open(y_file) as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='"')
    y = []
    for row in r:
        for n in row:
            y.append(float(n))

    # print(y_data)


# print(x)

plt.plot(x,y)

plt.xlabel("Time [s]")
plt.ylabel("Angular velocity [deg/s]")
plt.show()
# plt.savefig('motor_step_PID.png')