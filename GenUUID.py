import uuid
import sys
import os

print("Python %s\n" % (sys.version,))

for x in range (1,21): #21 does 20 times, seems normal python thing?

	unique1=uuid.uuid4()
	#print('UUID[',x,']: ',unique1) #creates extra unneeded spaces
	#print("UUID %d" % (x)) #too complex
	print ('UUID [' + str(x).zfill(2) + ']: ' + str(unique1)) #simple string concatenate
	#                 1      2     3            4   5
	'''
		1 = str function converts decimal x to string
		2 = zfill pads the string to 2 chars
		3 = sets number of pad zeros
		4 = str function converts uuid unique1 to string
		5 = the uuid type var called unique1
	'''

os.system("echo.")	
os.system("pause")