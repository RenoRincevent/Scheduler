#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy
from math import gcd
from functools import reduce

############# Class Task #################

class task(object):
	periode = None
	deadline = None 
	charge = None
	name = None
	isPreempted = None
	missDeadline = None

	def __init__(self, periode = 0, deadline = 0, charge = 0, name ='', isPreempted = False, missDeadline = False):
		self.periode = periode
		self.deadline = deadline
		self.charge = charge
		self.name = name
		self.isPreempted = isPreempted
		self.missDeadline = missDeadline

	def toStr(self):
		print("Task {} has a period of {} and deadline of {} with charge of {}".format(self.name, self.periode, self.deadline, self.charge))

############### Class Microcycle ###############

class microcycle(object):
    time = None #duree du microcycle
    tasks = None #liste de tache dans le microcyle 
    resTime = None #temps non utilisé dans les microcycle
    
    def __init__(self,time = 0,tasks = [],resTime =0):
        self.time = time
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
def printHyperperiod(hyperperiod):
	for i in range(len(hyperperiod)):
		print("------------ {}".format(hyperperiod[i].time*i))
		for k in hyperperiod[i].tasks[:]:
			for l in range(0, k.charge):
				if k.missDeadline and l == k.charge - 1:
					print("-- {} /!\ Task miss deadline /!\ ".format(k.name))
				elif k.isPreempted and l== k.charge-1:
					print("-- {} ~~Preempted Task".format(k.name))
				else:
					print("-- {}".format(k.name))
		for j in range(0,hyperperiod[i].resTime):
			print("--")

def initHyperperiod(nbMicrocycle,ucycle):
	hyperperiod = []
	for i in range(0, nbMicrocycle):
		hyperperiod.append(microcycle(ucycle,[],ucycle))
	return hyperperiod
    
    
    
def main():
	inputFile = open(sys.argv[1])
	tasks = parse(inputFile)
	#if RM Scheduler
	tasks.sort(key=lambda task: task.periode)
	print("En triant les fonctions selon prio RM:")
	printTasksList(tasks)
	#TODO if DM Scheduler
	
	#Calcule du microcyle et de l'hyperperiode
	periodList = []
	for i in tasks[:]:
		periodList.append(i.periode)
	lcm = numpy.lcm.reduce(periodList) #temps de l'hyperperiode/macrocycle
	pgcd = reduce(gcd, periodList) #temps du microcycle

	#init de l'hyperperiod
	nbMicrocycle = int(lcm / pgcd)
	hyperperiod = initHyperperiod(nbMicrocycle,pgcd)
	
	#Placer les taches dans le tableau Hyperperiod
	for i in tasks[:]:
		it = int(i.periode / pgcd)
		j = 0
		while j < nbMicrocycle:
			if hyperperiod[j].resTime - i.charge < 0: #Cas ou toute la charge ne rentre pas, elle est preemptée
				k = j + 1
				hyperperiod[j].tasks.append(task(i.periode,i.deadline,hyperperiod[j].resTime,i.name,True))
				restCharge = i.charge - hyperperiod[j].resTime
				hyperperiod[j].resTime = 0
				while hyperperiod[k].resTime != 0 and restCharge > 0:
					if hyperperiod[k].resTime > restCharge: #Tout le reste de la charge rentre sans une nouvelle preemption
						hyperperiod[k].tasks.append(task(i.periode,i.deadline,restCharge,i.name))
						hyperperiod[k].resTime = hyperperiod[k].resTime - restCharge
						restCharge = 0
					else: #La tache sera de nouveau preemptée au moins une fois avant de pouvoir se finir
						restCharge = restCharge - hyperperiod[k].resTime
						hyperperiod[k].tasks.append(task(i.periode,i.deadline,hyperperiod[k].resTime,i.name,True))
						hyperperiod[k].resTime = 0
					k = k + 1
			else : 		
				hyperperiod[j].tasks.append(i)
				hyperperiod[j].resTime = hyperperiod[j].resTime - i.charge 
			j = j + it
			

	printHyperperiod(hyperperiod)
if __name__ == "__main__":
	main()
