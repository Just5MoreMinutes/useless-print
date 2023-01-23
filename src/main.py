"""
-> useless_print v0.0.1

### UPRINT
useless_print (uprint) does a bunch of useless stuff nobody really asked for. Hence the name.
You can use uprint to make it easier to make nice looking `print` statements including *all*
`RGB` and `HEX` values. Additionally you can decorate your outputs with all sorts of decorations
including bold, italic, underlined or striked-through text. All this can be done with the basic 
uprint syntax, which looks like this:\n\n

```
uprint("[red]Hello, [purple]World[reset]!")
uprint("[red]**Hello**, [purple]World[reset]!")
uprint("<...>")
```

Besides that uprint allows you to disable and re-enable print statements at any point throughout
the program. However, uprint statements can bypass this when `uprint.bypass_self()` is used at the
start of the program.\n\n

```
# blocked.py
block_print()
print("Hello, World!") # <- blocked statement
enable_print()
print("output") # <- re-enabled print

# uprint.py
uprint.bypass_self()
block_print()
print("This is not printed")
uprint("This is being printed")
```

uprint also allows to print something once a certain function is called or once it has ended.
Additionally, variables can be modified together with a print statement using `uprint.modify(<args>)`.
"""
#===============#
# GLOBAL VARS   #
#===============#
PRINT_DISABLED = False
BYPASS_SELF = False
MUTE_SELF = False
PRESETS = {}


#===============#
# IMPORTS       #
#===============#
from typing import Any
import sys
import os

import functools

import re
from time import sleep


#===============#
# DECORATORS    #
#===============#
def uprint_func(func):
    #: func = the function that wrapped
    #: func is being reused in functools wrapper
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        return func(*args, **kwargs)
    wrapper.has_been_called = False
    return wrapper


#===============#
# STYLE         #
#===============#
#: a function to implement RGB color options
def rgb(r,g,b,bg=False):
    """
    Can set text to any color on the rgb spectrum.
    USAGE:
        print("Hello" + rgb(255, 128, 0) + "World!")
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)

#: a function to convert HEX to RGB and then to color sequences
def hex(code,bg=False):
    """
    Can set text to any color.
    USAGE:
        print(hex(code='#ff66cc') + "Hello, World!")
    """
    tmp = tuple(int(code.strip('#')[i:i+2], 16) for i in (0, 2, 4))
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38, tmp[0],tmp[1],tmp[2])


#===============#
# UTILS         #
#===============#
def block_print():

    #: blocks any print output
    sys.stdout = open(os.devnull, 'w')

def enable_print():

    #: re-enables any print output
    sys.stdout = sys.__stdout__

def get_methods(_class):

    #: get all methods from a class
    return [i for i in dir(_class) if callable(getattr(_class, i)) and not i.startswith("__")]

def replace(item):

    #: define variable to store user-decided color
    col = Any

    #: check if item is in PRESETS dictionary
    if item not in PRESETS.keys() and 'rgb' in item:

        #: finds all digits in the given list 'item'
        _rgb = re.findall(r'\d+', item)

        #: convert to RGB
        col = rgb(_rgb[0], _rgb[1], _rgb[2])

    #: check if itrem is in PRESETS dictionary
    if item not in PRESETS.keys() and '#' in item:

        #: convert to HEX
        col = hex(item)
    
    #: item is in PRESETS dictionary
    for i in PRESETS.keys():

        #: check if any dictionary key is euqal to item and store color in return variable
        if i == item:
            col = PRESETS[i]
    return col

def extract(txt):
    col = re.findall(r'\[(.*?)\]', txt)
    b_i = re.findall(r'\*\*?(.*?)\*\*?', txt)
    und = re.findall(r'__(.*?)__', txt)
    cut = re.findall(r'~~(.*?)~~', txt)

@uprint_func
def uprint(txt):

    #: regex to find all '[', ']' and their contents
    regex = re.findall(r'\[(.*?)\]', txt)
    
    #: iterate over all instances of the indicators
    for i in regex:

        #: replace with corresponding color
        txt = txt.replace('['+i+']', replace(i))
    
    print(txt)
    

#===============#
# MAIN          #
#===============#
class uprint():

    cwd = Any
    tag = Any
    methods = Any

    @classmethod
    def help(get):
        print(rgb(77, 77, 255)+'==============='+rgb(204, 204, 204)+' UPRINT HELP '+rgb(77, 77, 255)+'===============')

    @classmethod 
    def setup(update):
        update.cwd = os.getcwd()
        update.tag = 'uprint_v0.1.1'
        update.methods = get_methods(uprint)

    @classmethod
    def bypass_self(get, bypass=False):

        #: automatically bypasses uprint statements even when prints are blocked
        BYPASS_SELF = bypass
        if BYPASS_SELF == True:

            #: get necessary vars
            _methods = get.methods.remove(i for i in ['help', 'setup', 'bypass_self'])

            #: runs at all times so no function can be missed - performance decrease
            while bypass == True:

                #: function has been called
                if [i.has_been_called for i in _methods]: enable_print()
                else: block_print() if PRINT_DISABLED == True else enable_print()

        else: ...
    
    @uprint_func
    @classmethod
    def call(get, txt, func, delay:int) -> str:
        """
        uprint.call(<txt>, <func-name>, <delay>)
        """
        if PRINT_DISABLED == False and MUTE_SELF == False:
            print(txt)

            #: use delay
            sleep(delay) if delay != None else sleep(0)

            #: call func
            func()

        return get.tag

    @uprint_func
    @classmethod
    def modify(get, txt, var, val):
        """
        uprint.modify(<txt>, <var>, <value>)
        """
        return get.tag


#===============#
# INITIALIZE    #
#===============#
uprint = uprint()