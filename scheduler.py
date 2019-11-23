#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy

############# Class Task #################

class task(object):
	periode = None
	deadline = None
	charge = None
	name = None

	def __init__(self, periode, deadline, charge, name):
		self.periode = periode
		self.deadline = deadline
		self.charge = charge
		self.name = name

	def toStr(self):
		print("Task {} has a period of {} and deadline of {} with charge of {}".format(self.name, self.periode, self.deadline, self.charge))

############### Class Microcycle ###############

class microcycle(object):
    start = None #debut ou la tache démarre
    tasks = None #liste de tache dans le microcyle 
    resTime = None #temps non utilisé dans les microcycle
    
    def __init__(self,start,tasks,resTime):
        self.start = start
        self.tasks = tasks
        self.resTime = resTime

##############################

def parse(tasksFile):
	tasks = []
	for line in tasksFile:
		if line.startswith(('#')): continue
		if line.startswith('t'):
			taskDescription = line[2:].rstrip('\n').split(' ')
			tasks.append(task(int(taskDescription[0]),int(taskDescription[1]),int(taskDescription[2]),taskDescription[3]))
	return tasks

########## Debug Fonction ##########
def printTasksList(tasks):
	for i in range(len(tasks)): 
		tasks[i].toStr()
####################################
#def tableRM(tasks): #[periode,deadline,charge,nom]
#    sorted(tasks, key=getKey)
#    lcm = numpy.lcm.reduce(tasks.periode)
#    print(lcm)
    
    
    
def main():
	inputFile = open(sys.argv[1])
	tasks = parse(inputFile)
	printTasksList(tasks)
	tasks.sort(key=lambda task: task.periode)
	print("En triant les fonctions :")
	printTasksList(tasks)
	
	#TODO calculer microcycle
	#TODO calculer macrocycle/hyperperiod : creer un tableau de microcycle grace au calcul
	#TODO  placer les taches dans le tableau Hyperperiod
    
if __name__ == "__main__":
	main()
