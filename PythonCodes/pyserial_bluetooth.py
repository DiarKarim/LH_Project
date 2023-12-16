import serial 


ser = serial.Serial('COM9', 9600, timeout=0,parity=serial.PARITY_ODD, rtscts=1)
s = ser.read(200)       # read up to one hundred bytes or as much is in the buffer

print(s)