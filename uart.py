import serial 
import time
s = serial.Serial('/dev/ttyUSB0', 9600)

print(s.name)
while (True):
	x = s.readline().decode('utf-8')
	print(x, end="")
	#time.sleep(5)
s.close()
