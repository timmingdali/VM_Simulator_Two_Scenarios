#Author: Tim
#2017-07-05
#Modified by Ginny


import matplotlib.pyplot as plt
import numpy as np


utilization_dir = "results/resourceUtilization/"
filename = utilization_dir + "Multi Resource alignment discard/" + "memory"

with open (filename, 'r') as f:
    list = []
    for line in f:
        value = line.rstrip('\n')
        delay = float(value)
        list.append(delay)

sorted_data = np.sort(list)

yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

plt.plot(sorted_data, yvals, label = "Multi-Resource" )
plt.legend()


filename = utilization_dir + "First Fit Discard/" + "memory"

with open (filename, 'r') as f:
    list = []
    for line in f:
        value = line.rstrip('\n')
        delay = float(value)
        list.append(delay)

sorted_data = np.sort(list)

yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

plt.plot(sorted_data, yvals, label = "First Fit" )
plt.legend()



plt.title('Memory Utilization CDF')
plt.xlabel('Memory Utilization')
plt.ylabel('CDF')


plt.show()








'''


THE CODE BELOW GENERATES A CDF FOR CPU Utilization


'''






filename = utilization_dir + "Multi Resource alignment/" + "CPU"

with open (filename, 'r') as f:
    list = []
    for line in f:
        value = line.rstrip('\n')
        delay = float(value)
        list.append(delay)

sorted_data = np.sort(list)

yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

plt.plot(sorted_data, yvals, label = "Multi-Resource" )
plt.legend()



filename = utilization_dir + "First Fit/" + "CPU"

with open (filename, 'r') as f:
    list = []
    for line in f:
        value = line.rstrip('\n')
        delay = float(value)
        list.append(delay)

sorted_data = np.sort(list)

yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

plt.plot(sorted_data, yvals, label = "First Fit" )
plt.legend()


plt.title('CPU Utilization CDF')
plt.xlabel('CPU Utilization')
plt.ylabel('CDF')


plt.show()



'''


THE CODE BELOW GENERATES A CDF FOR VM REQUEST PLACEMENT DELAY


'''


latency_dir = "results/requestLatency/"

filename = latency_dir + "Multi Resource alignment"

with open (filename, 'r') as f:
    list = []
    for line in f:
        value = line.rstrip('\n')
        delay = int(value)
        if delay >= 10:
            list.append(delay)

sorted_data = np.sort(list)

yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

plt.plot(sorted_data, yvals, label = "Multi-Resource" )
plt.legend()


filename = latency_dir + "First Fit"

with open (filename, 'r') as f:
    list = []
    for line in f:
        value = line.rstrip('\n')
        delay = int(value)
        if delay >= 10:
            list.append(delay)

sorted_data = np.sort(list)

yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)

plt.plot(sorted_data, yvals, label = "First Fit" )
plt.legend()



plt.title('VM PLACEMENT LATENCY')
plt.xlabel('Placement Delay (s)')
plt.ylabel('CDF')

plt.show()




'''


THE CODE BELOW GENERATES GRAPH FOR UNUSED MACHINES


'''



unused_dir = "results/unusedMachines/"


filename = unused_dir + "Multi Resource alignment"

timelist = []
numberOfVMList = []
with open (filename, 'r') as f:
    for line in f:
        value = line.rstrip('\n').split('\t')
        time = int(value[0])
        numberOfVM = int(value[2])
        timelist.append(time)
        numberOfVMList.append(numberOfVM)
plt.plot(timelist, numberOfVMList, label = "Multi-Resource" )
plt.legend()


filename = unused_dir + "First Fit"

timelist = []
numberOfVMList = []
with open (filename, 'r') as f:
    for line in f:
        value = line.rstrip('\n').split('\t')
        time = int(value[0])
        numberOfVM = int(value[2])
        timelist.append(time)
        numberOfVMList.append(numberOfVM)

plt.plot(timelist, numberOfVMList, label = "First Fit" )
plt.legend()


plt.title('Unused Machines Number Timeline')
plt.ylabel('# of Un-used Machines')
plt.xlabel('Time (s)')
plt.show()










