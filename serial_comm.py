## Program: Serial Communication
## Project: Junior Design ARM 09
## Author: Calder Wilson

import serial

def send_code(g_code):
    """Send g-code line by line over serial port"""
    ser = serial.Serial('COM5', 9600)
    #ser.write(line.encode())
    ser.close()
    return
