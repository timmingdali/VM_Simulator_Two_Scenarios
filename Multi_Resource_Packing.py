
# Written by Siqi
# 2017-06-30
# Modefied by Ginny

from Placement import Placement
import sys
import time


def getKey(task):
    return task.arrival_time

class Multi_resource_alignment(Placement):
    def __init__(self):
        super(Multi_resource_alignment, self).__init__()
        self.requestLatency = []

    def VMplacement(self):
        start_time = time.time()

        current_time = 0
        unplaced_tasks = self.tasks[:]
        backlogged_tasks = []

        machine_empty = False
        enough_resource = True
        firstFailureAlready = False

        while unplaced_tasks or not machine_empty:
            machine_empty = self.updateMachines(current_time)
            while unplaced_tasks:
                if unplaced_tasks[0].arrival_time <= current_time:
                    backlogged_tasks.append(unplaced_tasks.pop(0))
                else:
                    break

            if backlogged_tasks:
                for m in self.cluster:
                    while True:
                        alignment_score = 0
                        task_index = 0
                        placed = False
                        for index, task in enumerate(backlogged_tasks):
                            if m.availMem >= task.mem and m.availCPU >= task.cpu:
                                placed = True
                                task_score = (m.availMem / m.mem) * (task.mem / m.mem) \
                                              + (m.availCPU / m.CPU) * (task.cpu / m.CPU)
                                if task_score > alignment_score:
                                    alignment_score = task_score
                                    task_index = index


                        if placed:
                            backlogged_tasks[task_index].hostMachine = m.machineID
                            backlogged_tasks[task_index].placement_time = current_time
                            m.placeTask(backlogged_tasks[task_index])
                            self.requestLatency.append(current_time - task.arrival_time)
                            print "place task", backlogged_tasks[task_index].arrival_time, backlogged_tasks[task_index].duration, \
                                backlogged_tasks[task_index].cpu, backlogged_tasks[task_index].mem, "in machine",\
                                backlogged_tasks[task_index].hostMachine, "at time", current_time
                            backlogged_tasks.pop(task_index)

                        if not placed:
                            break

            else:
                if current_time % 1 == 0 or (len(unplaced_tasks) == 0):
                    self.getResults(current_time)
                current_time += 1
                continue

            for task in backlogged_tasks:
                if task.hostMachine == None:
                    unplaced_tasks.append(task)
                    enough_resource = False

            backlogged_tasks = []

            if not enough_resource:
                print "Multi-Resource Packing: not enough resource for all tasks, time", current_time
                unplaced_tasks.sort(key=getKey, reverse=False)
                if not firstFailureAlready:
                    self.getFirstFailureResult()  # First Failure Utilization Check
                    firstFailureAlready = True

            if current_time % 10 == 0 or (len(unplaced_tasks) == 0):
                self.getResults(current_time)
            current_time += 1

        end_time = time.time()
        self.getTimeResult(end_time - start_time)



    def getResults(self, current_round):
        super(Multi_resource_alignment, self).getResults(current_round)

    def __str__(self):
        return "Multi Resource alignment"
