# -*- coding: utf-8 -*-
"""
A module for demonstrating exceptions
Created on Fri Feb  8 09:12:51 2019

@author: Aline
"""
import sys

def convert(s):
    '''Convert to an integer'''
    try:
        x = int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}"\
              .format(str(e)), file = sys.stderr)
        return -1
    return x
