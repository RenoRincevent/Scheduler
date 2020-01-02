#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def parse(tasksFile):
	tasks = []
	uniqueTasks = []
	next(tasksFile)
	for line in tasksFile:
		if line.startswith(('--')):
			tasks.append('while')
		else:
			task = line.split('[')
			if task[0] not in uniqueTasks:
				uniqueTasks.append(task[0])
			tasks.append(task[0])
	return (tasks,uniqueTasks)


def main():
	inputFile = open(sys.argv[1])
	StaticS = open('Static_scheduling.c', 'w')
	tasks,uniqueTasks = parse(inputFile)

	StaticS.write('''#define TC_DIV TC_CLOCK2
	''')
	for u in uniqueTasks[:]:
		StaticS.write('''
void {}()'''.format(u))
		StaticS.write('{}')#TODO générér les accolades !!! => {}

	#Initialize main timer
	StaticS.write('''
	
int main(){
	TC0_CCR = TC_CLKDIS;
	TC0_CMR = TC_DIV | TC_CPCTRG;
	TC0_RC = 10_MILLISECOND;
	TC0_CCR = TC_SWTRG | TC_CLKEN;

	while(1){''')

	#loop
	for t in tasks[:]:
		if t == 'while':
			StaticS.write('''
			while(!(TC0_SR & TC_CPCS));''')
		else:
			StaticS.write('''
			{}();'''.format(t))

	#end of loop
	StaticS.write('''
	}
}''')

if __name__ == "__main__":
	main()
