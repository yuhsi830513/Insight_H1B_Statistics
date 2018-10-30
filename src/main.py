# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:23:22 2018

@author: yuhsiC
"""

import os, sys, H1B

#read path parameter from command line in run.sh
input_path = sys.argv[-3]
occupation_file = sys.argv[-2]
state_file = sys.argv[-1]

#or set up relative path in Python script
#dirname = os.path.dirname(__file__)
#input_file = os.path.join(dirname, '../input/h1b_input.csv')
#occupation_file = os.path.join(dirname, '../output/top_10_occupations.txt')
#state_file = os.path.join(dirname, '../output/top_10_states.txt')

for input_file in os.listdir(input_path):
	if 'csv' not in input_file:
	    print('Escaped {} since it is not a csv file.'.format(input_file.split('/')[-1]))
	else:
	    #Initialize an h1b object
	    h1b_counter = H1B.H1B(input_file, occupation_file, state_file)
	    #start counting and store the result
	    h1b_counter.execute()
