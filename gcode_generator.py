## Program: G-code Generator
## Project: Junior Design ARM 09
## Author: Calder Wilson

# List of G-Codes
# G00	Rapid positioning
# G01	Linear interpolation
# G90	Absolute programming
# G91	Incremental programming
# G20	Programming in inches
# G21	Programming in millimeters
# M02	End of program
# M06	Automatic tool change

import matplotlib.pyplot as plt
import numpy as np

def choose_units():
    """Set units for program to be in mm or inches"""
    usrin = input("Type in or mm: ")
    if usrin == 'mm':
        return("G21")
    return("G20")

def choose_type():
    """Sets program to be in absolute or incremental"""
    usrin = input("Type a or i: ")
    if usrin == 'i':
        return("G91")
    return("G90")

def dot_image(array):
    """Generate g-code for a dot image from an array"""
    g_code = []
    for i in range(np.size(array,axis=0)):
        g_code.append('G00 X' + str(array[i,0]) + ' Y' + str(array[i,1]) + ' Z1.0')
        g_code.append('G00 X' + str(array[i,0]) + ' Y' + str(array[i,1]) + ' Z0.0')
    return g_code

def line_image(array):
    """Generate g-code for a line-image from an array"""
    g_code = ['G00 X' + str(array[0,0]) + ' Y' + str(array[0,1]) + ' Z1.0']
    for i in range(0,np.size(array,axis=0)):
        g_code.append('G01 X'+ str(array[i,0]) + ' Y' + str(array[i,1]) + ' Z0.0')
    return g_code

def main(mode,array=None):
    """Main function of the program.
    mode = 'sound', 'face', or 'demo'
    array = numpy array conatining x,y coordinates to be plotted"""
    g_code = []     # List to hold g-code commands
    if mode == 'demo':
        with open('demo.txt') as f: # Read demo g_code from file, remove '\n'
            g_code = f.read().splitlines()
    elif mode == 'sound':
        g_code = line_image(array)
    elif mode == 'face':
        g_code = dot_image(array)

    # Print the g_code to a text file
    f = open('gcode.txt', 'w')  #
    f.write('%' + mode + '\n')
    f.write('G20 G90\n')
    for i in g_code:
        f.write(str(i) + '\n')
    f.write('M02\n%\n')
    f.close()
    return g_code
