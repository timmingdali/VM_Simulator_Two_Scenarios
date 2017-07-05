
# Written by Siqi
# 2017-06-30

from Placement import Placement



def getKey(task):
    return task.arrival_time

class FirstFit (Placement):
    def __init__(self):
        super(FirstFit, self).__init__()
        self.requestLatency = []

    def VMplacement(self):
        current_time = 0
        unplaced_tasks = self.tasks[:]
        backlogged_tasks = []

        machine_empty = False
        enough_resource = True

        while unplaced_tasks or not machine_empty:
            machine_empty = self.updateMachines(current_time)

            while unplaced_tasks:
                if unplaced_tasks[0].arrival_time <= current_time:
                    backlogged_tasks.append(unplaced_tasks.pop(0))
                else:
                    break
            if backlogged_tasks:
                for task in backlogged_tasks:
                    for m in self.cluster:
                        if m.availMem >= task.mem and m.availCPU >= task.cpu:
                            m.placeTask(task)
                            task.placement_time = current_time
                            task.place_latency = current_time -task.arrival_time
                            self.requestLatency.append(current_time - task.arrival_time)
                            task.hostMachine = m.machineID
                            print "place task", task.arrival_time, task.duration, \
                                task.cpu, task.mem, "in machine", task.hostMachine, "at time", current_time
                            break
            else:
                if current_time % 10 == 0 or (len(unplaced_tasks) == 0):
                    self.getResults(current_time)
                current_time += 1
                continue

            for task in backlogged_tasks:
                if task.hostMachine == None:
                    unplaced_tasks.append(task)
                    enough_resource = False

            backlogged_tasks = []


            if not enough_resource:
                print "First Fit Discard: not enough resource for all tasks, time", current_time
                unplaced_tasks.sort(key=getKey, reverse=False)

            if current_time % 1 == 0 or (len(unplaced_tasks) == 0):
                self.getResults(current_time)
            current_time += 1



    def getResults(self, current_round):
        super(FirstFit, self).getResults(current_round)

    def __str__(self):
        return "First Fit"
