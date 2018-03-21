import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600)   # open serial port that Arduino is using
if ser.isOpen():
     print(ser.name + ' is open...')

def sukses():
	cmd='a'
	ser.write(cmd.encode('ascii')+'\r\n')

def gagal():
	cmd='b'
	ser.write(cmd.encode('ascii')+'\r\n')