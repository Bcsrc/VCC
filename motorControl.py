#! /usr/bin/python2.7

import serial
class MotorControl:

    ser = serial.Serial()

    def __init__(self):
        #self.ser = serial.Serial()
        self.ser.port = "COM4" #/dev/pts/3  /dev/ttyUSB0"
        print self.ser.portstr
        self.ser.baudrate = 2400
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_TWO
        self.ser.open()
    def forward(self):
        self.ser.write("\x01\x6f\x6f")
        
    def backward(self):
        self.ser.write("\x01\x5f\x5f")
        
    def left(self):
        #self.ser.write("x01\x7f\x6f")
        self.ser.write("\x01\x5f\x6f")
        
    def right(self):
        #self.ser.write("x01\x6f\x7f")
        self.ser.write("\x01\x6f\x5f")
        
    def stop(self):
        self.ser.write("\x01\x7f\x7f") 

    def coast(self):
        self.ser.write("\x01\x00\x00") 

