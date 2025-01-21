# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:21:47 2023

@author: Paul Namalomba
"""

# some python modules
import sympy as sym
import pandas as pd
import numpy as np
import re
import sys
import time
from itertools import groupby

# input prompt to put in your simulatenous equations
print("******Simultaneous equations solver******")
print("-----------------------------------------")
print("-!your LINEAR equation set must be a two-variable set")
eq_type_input = "two"
# try:
#     print("--------------------------------------")
#     print("-|your LINEAR equation set must be a two-variable set")
#     eq_type_input = str(input("Is your LINEAR equation set a three- or two-variable set?: "))
#     print(">processing your inputs, get ready to feed in your equations")
#     time.sleep(1)
# except Exception as b:
#     print("{}".format(b))
# print("<passed! feed in your equations")

# acceptable answers to above
acceptable_strings_types = ["Two", "two", "2"]
#"three", "3", "Three", 

# conditioning the answers and setting up the eqaution string input
equation_set = []
while eq_type_input in acceptable_strings_types:
    try:
        # two-variable, two-linear form
        if eq_type_input in acceptable_strings_types[:3]:
            eq_input1 = str(input("->equation 1: "))
            eq_input2 = str(input("->equation 2: "))
            equation_set.append(eq_input1)
            equation_set.append(eq_input2)
        # three variable, threee linear form
        # elif eq_type_input in acceptable_strings_types[3]:
        #     eq_input1 = str(input("->equation 1: "))
        #     eq_input2 = str(input("->equation 2: "))
        #     eq_input3 = str(input("->equation 3: "))
        #     equation_set.append(eq_input1)
        #     equation_set.append(eq_input2)
        #     equation_set.append(eq_input3)
    except Exception as e:
        print("-|{} when trying to parse your equation types".format(e))
        print("-|exiting, re-run the code please")
        continue
    break

from sub_modules import solver
solver.solver(equation_set)