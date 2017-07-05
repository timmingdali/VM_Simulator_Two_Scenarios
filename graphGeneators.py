#Author: Tim
#2017-07-05
#Modified by Ginny


import matplotlib.pyplot as plt
import numpy as np

trace = 'Workload_Traces_test'

time_dir = "results/time_elapsed"
utilization_dir = "results/resourceUtilization/"
firstFailure_dir = "results/firstFailure/"
# filename = utilization_dir + "Multi Resource alignment discard/" + "memory"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n')
#         delay = float(value)
#         list.append(delay)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "Multi-Resource" )
# plt.legend()
#
#
# filename = utilization_dir + "First Fit Discard/" + "memory"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n')
#         delay = float(value)
#         list.append(delay)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "First Fit" )
# plt.legend()
#
#
#
# plt.title('Memory Utilization CDF')
# plt.xlabel('Memory Utilization')
# plt.ylabel('CDF')
#
#
# plt.show()
#
#
#
#
#
#
#
#
# '''
#
#
# THE CODE BELOW GENERATES A CDF FOR CPU Utilization
#
#
# '''
#
#
#
#
#
#
# filename = utilization_dir + "Multi Resource alignment/" + "CPU"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n')
#         delay = float(value)
#         list.append(delay)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "Multi-Resource" )
# plt.legend()
#
#
#
# filename = utilization_dir + "First Fit/" + "CPU"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n')
#         delay = float(value)
#         list.append(delay)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "First Fit" )
# plt.legend()
#
#
# plt.title('CPU Utilization CDF')
# plt.xlabel('CPU Utilization')
# plt.ylabel('CDF')
#
#
# plt.show()
#
#
#
# '''
#
#
# THE CODE BELOW GENERATES A CDF FOR VM REQUEST PLACEMENT DELAY
#
#
# '''
#
#
# latency_dir = "results/requestLatency/"
#
# filename = latency_dir + "Multi Resource alignment"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n')
#         delay = int(value)
#         if delay >= 10:
#             list.append(delay)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "Multi-Resource" )
# plt.legend()
#
#
# filename = latency_dir + "First Fit"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n')
#         delay = int(value)
#         if delay >= 10:
#             list.append(delay)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "First Fit" )
# plt.legend()
#
#
#
# plt.title('VM PLACEMENT LATENCY')
# plt.xlabel('Placement Delay (s)')
# plt.ylabel('CDF')
#
# plt.show()
#
#
#
#
# '''
#
#
# THE CODE BELOW GENERATES GRAPH FOR UNUSED MACHINES
#
#
# '''
#
#
#
# unused_dir = "results/unusedMachines/"
#
#
# filename = unused_dir + "Multi Resource alignment"
#
# timelist = []
# numberOfVMList = []
# with open (filename, 'r') as f:
#     for line in f:
#         value = line.rstrip('\n').split('\t')
#         time = int(value[0])
#         numberOfVM = int(value[2])
#         timelist.append(time)
#         numberOfVMList.append(numberOfVM)
# plt.plot(timelist, numberOfVMList, label = "Multi-Resource" )
# plt.legend()
#
#
# filename = unused_dir + "First Fit"
#
# timelist = []
# numberOfVMList = []
# with open (filename, 'r') as f:
#     for line in f:
#         value = line.rstrip('\n').split('\t')
#         time = int(value[0])
#         numberOfVM = int(value[2])
#         timelist.append(time)
#         numberOfVMList.append(numberOfVM)
#
# plt.plot(timelist, numberOfVMList, label = "First Fit" )
# plt.legend()
#
#
# plt.title('Unused Machines Number Timeline')
# plt.ylabel('# of Un-used Machines')
# plt.xlabel('Time (s)')
# plt.show()
#
#
#
# '''
#
#
# THE CODE BELOW GENERATES A CDF FOR CPU UTILIZATION DURING FIRST HIT FAILURE
#
#
# '''
#
# filename = firstFailure_dir + "Multi Resource alignment"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n').split('\t')
#         CPU_usage = float(value[1])
#         list.append(CPU_usage)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "Multi-Resource" )
# plt.legend()
#
#
#
# filename = firstFailure_dir + "First Fit"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n').split('\t')
#         CPU_usage = float(value[1])
#         list.append(CPU_usage)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "First Fit" )
# plt.legend()
#
#
# plt.title('First Failure CPU Utilization CDF ' + trace)
# plt.xlabel('CPU Utilization')
# plt.ylabel('CDF')
#
#
# plt.show()
#
# '''
#
#
# THE CODE BELOW GENERATES A CDF FOR MEMORY UTILIZATION DURING FIRST HIT FAILURE
#
#
# '''
#
#
#
# filename = firstFailure_dir + "Multi Resource alignment"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n').split('\t')
#         CPU_usage = float(value[2])
#         list.append(CPU_usage)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "Multi-Resource" )
# plt.legend()
#
#
#
# filename = firstFailure_dir + "First Fit"
#
# with open (filename, 'r') as f:
#     list = []
#     for line in f:
#         value = line.rstrip('\n').split('\t')
#         CPU_usage = float(value[2])
#         list.append(CPU_usage)
#
# sorted_data = np.sort(list)
#
# yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
#
# plt.plot(sorted_data, yvals, label = "First Fit" )
# plt.legend()
#
#
# plt.title('First Failure Memory Utilization CDF ' + trace)
# plt.xlabel('Memory Utilization')
# plt.ylabel('CDF')
#
#
# plt.show()


'''


THE CODE BELOW GENERATES A GRAPH FOR ALGORITHM EFFICIENCY


'''
filename = time_dir

with open (filename, 'r') as f:
    algorithms = []
    time = {}

    with open(filename, 'r') as f:
        for line in f:
            result = line.rstrip('\n').split('\t')
            if result[0] not in algorithms:
                algorithms.append(result[0])
                time_ = []
                time_.append(float(result[1]))
                time[result[0]] = time_
            else:
                time[result[0]].append(float(result[1]))

for element in algorithms:
    plt.plot(time.get(element), label="%s" % element)

plt.title('Algorithm Efficiency')
plt.xticks([0,1,2], ['Workload_Traces_test','Actual_Workload_Traces','Modified_Workload_Traces'], rotation=17)
plt.xlabel('Workload Traces')
plt.ylabel('Time Elapsed')
plt.legend()

plt.show()
