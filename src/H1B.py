# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:23:22 2018

@author: yuhsiC
"""
from collections import Counter
import csv, operator


class H1B:
    def __init__(self, infile, occupation_file, state_file):
        """
        Input:
            infile: path to input csv file
            occupation_file: path to output occupation statistics
            state_file: path to output state statistics
        Instance Variable:
            self.infile: same as infile
            self.out_occupation: occupation_file
            self.out_state: state_file
            self.interest_cols: dictionary to store wanted data
            self.total_certified: total number of certified applications
        """
        self.infile = infile
        self.out_occupation = occupation_file
        self.out_state = state_file
        self.interest_cols = {"states": [], "occupations": []}
        self.total_certified = 0
       
        
    def readCSV(self):
        """
        Read and preprocess the data
        """
        with open(self.infile, "r", encoding = "utf-8") as f:
            reader = csv.reader(f, delimiter=';')            
            headers = next(reader, None)   
            
            #Handle the case if there's small difference between header names
            #I.e. LCA_CASE_SOC_NAME (found in input examples) is the same as SOC_NAME
            interest_fields = {}
            for idx, field in enumerate(headers):
                if "SOC_NAME" in field.upper(): 
                    interest_fields.update({field:"occupations"})
                elif ("WORK" in field.upper()) and ("_STATE" in field.upper()):
                    interest_fields.update({field:"states"})
                elif ("STATUS") in field.upper():
                    status_idx = idx

            #if application certified, append state and occupation in to list         
            for row in reader:
                if row[status_idx].lower() == 'certified':
                    self.total_certified += 1
                    loc = ""    
                    for h, v in zip(headers, row):
                        if (h in interest_fields) and (v != loc) and (v != ""):
                            self.interest_cols[interest_fields[h]].append(v.upper())
                            if ("state" in h.lower()) and (loc is ""): #handle the case if location 1 and 2 are the same
                                loc = v
                       
                        
    def execute(self):
        """
        workflow: 
            1. read and preprocess data: H1B.readCSV()
            2. count
            3. write results to files: H1B.toTXT(state_list, occupation_list)
            
        """
        self.readCSV()
        
        #count, sort and find top 10
        state_counter = Counter(self.interest_cols["states"])
        most_common_states = sorted(sorted(state_counter.items(),
                                           key = operator.itemgetter(0)), 
                                    key = operator.itemgetter(1),
                                    reverse=True)[:10]
        occu_counter = Counter(self.interest_cols["occupations"])
        most_common_occupations = sorted(sorted(occu_counter.items(),
                                                key = operator.itemgetter(0)), 
                                         key = operator.itemgetter(1),
                                         reverse=True)[:10]
        #store results
        self.toTXT(most_common_states, most_common_occupations)
        
    
    def toTXT(self, states, occupations):
        """
        store the most 10 common states and occpations into txt files.
        Input: 
            states: List(Tuples(String, Int))
            occupations: List(Tuples(String, Int))
        """
        with open(self.out_state, "w+") as out:
            out.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
            for state, num in states:
                out.write("{};{};{:.1f}%\n".format(state, num, 100*num/self.total_certified))
                
                
        with open(self.out_occupation, "w+") as out:
            out.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
            for occupation, num in occupations:
                out.write("{};{};{:.1f}%\n".format(occupation, num, 100*num/self.total_certified))
            
            
        
        