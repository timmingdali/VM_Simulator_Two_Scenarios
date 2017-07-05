import math
import random
from scipy.stats import truncnorm
import numpy as np

request_number = 100
deploy_size_mean = 30
deploy_size = np.random.poisson(deploy_size_mean, request_number)
inter_arrival_time = np.random.poisson(2, request_number)
instance_type = {0: [1, 0.5], 1: [1,1], 2: [1,2], 3: [2,4], 4:[2,8],5:[4,16],6:[8,32]}

start_time = 0
arrival_time = np.zeros(request_number)
for i in range(request_number):
    arrival_time[i] = start_time
    start_time = arrival_time[i] + inter_arrival_time[i]

print arrival_time

workload = "Workloads/Workload_Traces_test"
with open(workload, 'w') as f:
    for i in range(request_number):
        count = 0
        deploy_number = deploy_size[i]
        duration = np.random.poisson(1000, deploy_number)
        type_num = np.random.randint(0, 7, deploy_number)
        while count < deploy_number:
            f.write("%d\t%d\t%d\t%f\n" % (arrival_time[i], duration[count], \
                                          instance_type[type_num[count]][0], instance_type[type_num[count]][1]))
            count += 1

pm_number = 200
cpu = 10
memory = 40
with open("Cluster_test", 'w') as f:
    for i in range(pm_number):
        f.write("%d\t%d\t%d\n" % (i+1, cpu, memory))

pm_number = 100
cpu = 32
memory = 100000
with open("Cluster", 'w') as f:
    for i in range(pm_number):
        f.write("%d\t%d\t%d\n" % (i+1, cpu, memory))