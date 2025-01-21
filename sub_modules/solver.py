#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:46:37 2025

@author: kb
"""
# some python modules
import sympy as sym
import pandas as pd
import re
import sys
import time
from itertools import groupby

# this is the .py that has all supporter functions
from sub_modules import methods

def solver(eq_set):
    print("-----------------------------------------")
    print(">starting the solver")
    # x,y = sym.symbols('x,y')
    admissible_x = ["x", "X", "y", "Y"]
    admissible_y = ["y", "y", "z", "Z"]
    if len(eq_set) == 2:
        eq_solver_list = []
        for each_eqn in eq_set:
            # split each equation into x and y and extract the alpha and numeric pairs 
            # i.e 2.0x is a pair ['2.0', 'x'] is list dtype
            eq_raw_list = methods.finalise_equation(each_eqn)
            eq_vars_list = eq_raw_list[:2]
            eq_vars_list = sorted(eq_vars_list, key=lambda x: x[-1])
            eq_equate_list = eq_raw_list[2:]
            eq_vars_split = []
            for each_split in eq_vars_list:
                eq_vars_split.append(methods.extract_equation_pairs(each_split))
            eq_coeffs = [float(eq_vars_split[0][0]), float(eq_vars_split[1][0])]
            eq_vars = [str(eq_vars_split[0][1]), str(eq_vars_split[1][1])]
            eq_output = [float(eq_equate_list[0])]
            x,y = sym.symbols('{x_var},{y_var}'.format(x_var=str(eq_vars[0]), 
                                                       y_var=str(eq_vars[1])))
            eq_solve = sym.Eq((eq_coeffs[0]*x) + (eq_coeffs[1]*y), eq_output[0])
            eq_solver_list.append(eq_solve)
        x,y = sym.symbols('{x_var},{y_var}'.format(x_var=str(eq_vars[0]), 
                                                   y_var=str(eq_vars[1])))
        result = sym.solve([eq_solver_list[0],eq_solver_list[1]],(x,y))
        for key in result:
            xy_values = result[key]
            xy_values = round(xy_values, 3)
            print("-|the {a}-root is {b}".format(a=key, b=xy_values))
    print("<done solving")
    print("-----------------------------------------")