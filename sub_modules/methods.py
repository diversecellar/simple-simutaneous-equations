#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:43:47 2025

@author: kb
"""
# some python modules
import sympy as sym
import pandas as pd
import numpy as np
import re
import sys
import time
from itertools import groupby

# this function separates an equation into it's "var" and "coefficient" pairs
# i.e '2.0x' is casted to ["2.0", "x"]
def extract_equation_pairs(equation_string) -> list:
    equation_pairs = []
    while isinstance(equation_string, str):
        for k, g in groupby(equation_string, str.isalpha):
            equation_pairs.append(''.join(g))
        break
    return equation_pairs

# code to remove whitespace, colons and commas from useable strings
def replace_unusual_chars(list_of_chars) -> list:
    list_of_chars_constructor = []
    unacceptable_chars = ["",",", ", ", " ", "  ", "   ", ",   ", ": ", ":"]
    for each_string in list_of_chars:
        if each_string not in unacceptable_chars:
            list_of_chars_constructor.append(each_string) 
    return list_of_chars_constructor

# code for the computer to join if a '-' is separate from the next numeric digit
def accumulate_math_symbols(x) -> list:
    new_x = []
    temp = None
    if isinstance(x, list):
        for i in x:
            if temp:
                i = temp+i
                temp = None
            if i == '−' or i == '-':
                temp = "-"            
                continue
            elif i == '+':
                temp = "+"
                continue
            new_x.append(i)
    return new_x

# code to split alphanumeric combined strings into single data types
def split_alphanumerics(name_of_str) -> list:
    regex = re.compile(r'(^[1-9]\d*$|\s+)')
    re_string_list = regex.split(name_of_str)
    string_list = replace_unusual_chars(re_string_list)
    string_list = accumulate_math_symbols(string_list)
    # string_list = sorted(string_list, key=lambda x: x[-1])
    # return the list
    output_list = []
    for each_string in string_list:
        string_out = replace_hyphens(each_string)
        output_list.append(string_out)
    return output_list

# replace weird hyphens
def replace_hyphens(str_name):
    if "−" in str_name:
        output = str_name.replace("−", "-")
    else:
        output = str_name
    return output

def finalise_equation(name_of_equation_string):
    # searching the index of '=' in equation to put the equation logic in perspective
    equation_as_list = split_alphanumerics(name_of_equation_string)
    indexes = []
    if isinstance(equation_as_list, list):
        index_of_equals = equation_as_list.index('=')
        indexes.append(index_of_equals)
        for each_var in equation_as_list:
            try:
                constant = float(each_var)
                index_of_constant = equation_as_list.index(each_var)
                indexes.append(index_of_constant)
            except Exception as f:
                nobody_cares = f
        new_equation_list = []
        if indexes[0] == 1 and indexes[1] >= 2:
            first_var = equation_as_list[0]
            while indexes[1] == 2:
                second_var = equation_as_list[3]
                break
            while indexes[1] == 3:
                second_var = equation_as_list[2]
                break
            if "+" in second_var:
                second_var = second_var.replace("+", "-")
            else:
                second_var = second_var.replace("-", "+")
            constant_var = equation_as_list[indexes[1]]
            new_equation_list = [first_var, second_var, constant_var]
        elif indexes[0] == 2 and indexes[1] >= 3:
            first_var = equation_as_list[0]
            while indexes[1] == 3:
                second_var = equation_as_list[1]
                break
            constant_var = equation_as_list[indexes[1]]
            new_equation_list = [first_var, second_var, constant_var]
        elif indexes[0] == 1 and indexes[1] <= 1:
            first_var = equation_as_list[2]
            while indexes[1] == 0:
                second_var = equation_as_list[3]
                break
            constant_var = equation_as_list[indexes[1]]
            new_equation_list = [first_var, second_var, constant_var]
        elif indexes[0] == 2 and indexes[1] <= 1:
            first_var = equation_as_list[3]
            while indexes[1] == 0:
                second_var = equation_as_list[1]
                break
            while indexes[1] == 1:
                second_var = equation_as_list[0]
                break
            if "+" in second_var:
                second_var = second_var.replace("+", "-")
            else:
                second_var = second_var.replace("-", "+")
            constant_var = equation_as_list[indexes[1]]
            new_equation_list = [first_var, second_var, constant_var]
    return new_equation_list