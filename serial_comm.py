## Program: Serial Communication
## Project: Junior Design ARM 09
## Author: Calder Wilson

import serial
import time

def initalize():
    ser = serial.Serial('COM5', baudrate = 115200, timeout = 1)
    time.sleep(1)
    ser.write(b'%')
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
    return ser

def send_code(g_code = None):
    """Send g-code line by line over serial port"""
    usrin = input('Next line? ')

    if usrin == 'y':
        ser.write(b'G1 X1 Y0 Z1')
    time.sleep(1)
    if ser.in_waiting:
        print(ser.readline().decode('ascii'))

    return

def end():
    ser.close()
    return

ser = initalize()
send_code()
end()
