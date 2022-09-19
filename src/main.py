"""
useless_print ('up') does some useless stuff nobody asked for.
"""
#===============#
# IMPORTS       #
#===============#
from typing import Any
import sys
import os


#===============#
# STYLE         #
#===============#
#: a function to implement rgb color options
def rgb(r,g,b,bg=False):
    """
    Can set text to any color on the rgb spectrum.
    USAGE:
        print("Hello" + rgb(255, 128, 0) + "World!")
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)


#===============#
# UTILS         #
#===============#
def block_print():
    sys.stdout = open(os.devnull, 'w')

def enable_print():
    sys.stdout = sys.__stdout__


#===============#
# MAIN          #
#===============#
#: default useless_print function, no modifications etc
def uprint(txt, color, *tag, **id):
    str(txt)
    return [tag, id] and str(color + txt)


class upp:

    __tag = Any
    __id  = Any

    @classmethod
    def get_tag(add):

        block_print()
        print(uprint('hello', rgb(0,0,0), 'a', 1))
        add.__tag = uprint[0]
        add.__id  = uprint[1]
        enable_print()
        print(add.__id, add.__tag)


upp = upp()


upp.get_tag()


