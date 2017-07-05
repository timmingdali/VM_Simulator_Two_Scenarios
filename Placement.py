# Wriiten by Siqi
# 2017-06-30



class Placement(object):
    def __int__(self):
        super(Placement, self).__init__()

    def updateMachines(self, current_time):

        machine_empty = True

        for machine in self.cluster:
            if machine.beingUtilized:
                for task in list(machine.runningTasks):
                    if task.placement_time + task.duration <= current_time:
                        machine.removeTask(task, current_time)
                        machine.runningTasks.remove(task)
                        print "delete task", current_time, task.arrival_time, task.placement_time, task.duration, task.cpu, task.mem, "on machine", task.hostMachine

        for machine in self.cluster:
            if machine.beingUtilized:
                if not machine.runningTasks:
                    machine.beingUtilized = False

        for machine in self.cluster:
            if machine.beingUtilized:
                machine_empty = False

        return machine_empty

    def getResults(self, currentRound):

        self.availMachine = 0
        for machine in self.cluster:
            if machine.beingUtilized == False:
                self.availMachine += 1

        unusedMachine_dir = "results/unusedMachines/" + self.__str__()
        requestLatency_dir = "results/requestLatency/" + self.__str__()
        cpu_dir = "results/resourceUtilization/" + self.__str__() + "/" + "CPU"
        memory_dir = "results/resourceUtilization/" + self.__str__() + "/" + "memory"



        with open(unusedMachine_dir, 'a') as f:
            f.write("%d\t%s\t%d\n" %(currentRound, self.__str__(), self.availMachine))


        with open(memory_dir, 'a') as f:
            for machine in self.cluster:
                if machine.beingUtilized == True:
                    f.write("%f" % ((machine.mem - machine.availMem) / machine.mem))
                    f.write("\n")


        with open(cpu_dir, 'a') as f:
            for machine in self.cluster:
                if machine.beingUtilized == True:
                    f.write("%f" % ((machine.CPU - machine.availCPU) / machine.CPU))
                    f.write("\n")

        with open(requestLatency_dir, 'a') as f:
            for latency in self.requestLatency:
                f.write("%d\n" % (latency))

        self.requestLatency = []


    def getFirstFailureResult(self):

        firstFailureUtil_dir = "results/firstFailure/" + self.__str__()

        with open(firstFailureUtil_dir, 'w') as f:
            for machine in self.cluster:
                f.write("%d\t%.2f\t%.2f\n" % (machine.machineID, (machine.CPU - machine.availCPU)/machine.CPU \
                                                  ,(machine.mem - machine.availMem)/machine.mem) )

    def getTimeResult(self, time_elapsed):
        path = "results/time_elapsed"

        with open(path, 'a') as f:
            f.write("%s\t%f\n" % (self.__str__(), time_elapsed))
