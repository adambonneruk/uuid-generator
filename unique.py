import sys

from unique_help import help
from unique_generate import generate

###############################################################################
import os
os.system("cls")
###############################################################################

args = len(sys.argv) - 1 # number of arguments (minus the program itself)

if args == 0: #no arguments, just run with default single UUIDv4
	print("...zero")
	generate()
elif args == 2: #just one argument and parameter pair (number or version)
	print("...two")
	generate()
elif args == 4: #both version and number specified
	print("...four")
	generate()
else: #any other (wrong) number of arguments, display help
	help()
