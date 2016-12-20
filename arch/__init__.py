#!/usr/bin/env
"""

File:           /arch/__init__py
Author:         Josh Kaplan
Email:          contact@joshkaplan.org
Description:    A class defining a base architecture.

"""
import os


class BaseArchitecture(object):

    def __init__(self):
        pass




class console(object):

    def __init__(self):
        pass

    @staticmethod
    def log(s):
        if os.name.lower() == 'posix':
            print '\033[95m\033[1mWARNING\033[0m\033[1m - %s\033[0m\n' % (s)
        else:
            print s


    @staticmethod
    def warning(s):
        if os.name.lower() == 'posix':
            print '\033[93m\033[1mWARNING\033[0m\033[1m - %s\033[0m\n' % (s)
        else:
            print s


class helpers(object):

    def __init__(self):
        pass


    @staticmethod
    def is_constant(val):
        '''Returns true if the string value is a valid assembler constant, 
        False otherwise.'''

        # handle multiple syntaxes (plural?) of hex
        if val.lower().endswith('h'):
            val = '0x' + val[:-1]

        # determine number base
        if val.lower().startswith('0x'):
            base = 16
        elif val.lower().startswith('0'):  
            base = 8
        else:
            base = 10

        # attempt to convert to int, if exceptions return false
        try:
            return int(val, base) >= 0
        except ValueError:
            return False
        except:
            return False
 

    @staticmethod
    def resolve_constant(val):
        '''Returns the interger value of the string val. Returns None is any
        errors occur.'''
        if not helpers.is_constant(val):
            return None

        # handle multiple syntaxes (plural?) of hex
        if val.lower().endswith('h'):
            val = '0x' + val[:-1]

        # determine number base
        if val.lower().startswith('0x'):
            base = 16
        elif val.lower().startswith('0'):  
            base = 8
        else:
            base = 10

        # attempt to convert to int, if exceptions return None
        try:
            return int(val, base)
        except:
            return None

