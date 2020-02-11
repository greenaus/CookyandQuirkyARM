## Program: Command Parser
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
import serial

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

def dot_image(f,array):
    """Generate g-code for a dot image from an array"""
    f.write('G00 Z1.0\n')
    for i in range(np.size(array,axis=0)):
        f.write('X'+str(array[i,0]))
        f.write(' Y'+str(array[i,1])+'\n')
        f.write('Z0.0\n')
        f.write('Z0.1\n')
    return

def line_image(f,array):
    """Generate g-code for a line-image from an array"""
    f.write('G00 Z1.0\n')
    f.write('X'+str(array[0,0])+' Y'+str(array[0,1])+'\n')
    f.write('G01 Z0.0\n')
    for i in range(1,np.size(array,axis=0)):
        f.write('X'+str(array[i,0]))
        f.write(' Y'+str(array[i,1])+'\n')
    f.write('Z1.0\n')
    return

def serial_comm(filename):
    """Send g-code text file line by line over serial port"""
    ser = serial.Serial('COM3', 9600)
    fileIN = open(filename, "r")
    line = fileIN.readline()
    while line:
        line = fileIN.readline()
        ser.write(b(line))
    ser.close()
    return

def main(mode,array=None):
    """Main function of the program.
    mode = 'sound', 'image', or 'demo'
    array = numpy array conatining x,y coordinates to be plotted"""

    if mode == 'demo':
        #serial_comm('demo.txt')
        x = 1
    else:
        f = open('gcode.txt', 'w')
        f.write('%\nO1000\n')
        f.write('G20 G90\n')
        if mode == 'sound':
            line_image(f,array)
        elif mode == 'image':
            dot_image(f,array)
        f.write('M02\n%\n')
        f.close()
        #serial_comm('gcode.txt')
    return
