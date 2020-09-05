import sys
import re

from unique_help import help
from unique_generate import generate

###############################################################################
import os
os.system("cls")
###############################################################################

args = len(sys.argv) - 1 # number of arguments (minus the program itself)
print("args: " + str(args))
#set defaults
version = 4
count = 1
print("v: " + str(version))
print("c: " + str(count))

try:
	for i in range(1, args + 1): # 1 to the number of arguments
		if re.search(r"^(-v|--version)$",sys.argv[i]):
				version = sys.argv[i+1]
		if re.search(r"^(-c|--count)$",sys.argv[i]):
				count = sys.argv[i+1]

	print("V: " + str(version))
	print("C: " + str(count))
	print("------------------------------")

	if args == 0:
		generate()
	elif args == 2:
		print("generate")
	elif args == 4:
		print("generate")
	else:
		help()
except:
	help()