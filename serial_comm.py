## Program: Serial Communication
## Project: Junior Design ARM 09
## Author: Calder Wilson

import serial
import time
import audio_processing
import gcode_generator
import numpy as np

def initalize():
    ser = serial.Serial('COM5', baudrate = 115200, timeout = 1)
    time.sleep(3)
    ser.reset_input_buffer()
    # ser.write(b'%')
    # time.sleep(1)
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
    return ser

def send_code(g_code = None):
    """Send g-code line by line over serial port"""
    for i in g_code:
        ser.write((i + '\n').encode('utf-8'))
        time.sleep(0.5)
        while ser.in_waiting:
            print(ser.readline().decode('ascii'))
    while ser.in_waiting:
        print(ser.readline().decode('ascii'))

    return

my_audio = audio_processing.audio_main()
g_code = gcode_generator.main('sound', my_audio)
ser = initalize()
send_code(g_code)
ser.close()
