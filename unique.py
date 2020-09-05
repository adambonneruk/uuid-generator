import sys

from unique_help import help
from unique_generate import generate

###############################################################################
import os
os.system("cls")
###############################################################################

args = len(sys.argv) - 1 # number of arguments (minus the program itself)

if args == 0: #no arguments, just run with default single UUIDv4
	generate()
elif args == 2:
	print("...two")
elif args == 4:
	print("...four")
else: #any other (wrong) number of arguments, display help
	help()
'''
no arguments
	# nothing, just run with defaults
	print("zero")
one or less arguments
	# not enough for anything valid
	help()
	print("zero or one")
two argumnets
	# only valid scenario is help
	help()
	print("two")
three argumnets
	# could be just -v X or just -n X
	# unqiue -v 2
	print("three")
four arguments
	# invalid as missing a value for one flag
	help()
	print("four")
five arguments
	print("five")
six or more
	help
'''

''' DUMB CODE
if len(sys.argv) == 1: # default bahviour, just generate a single UUIdv4 (no arguments)
	outputUuidString=uuid.uuid4()
	print(outputUuidString)
else:
	if sys.argv[1] == '--help':
		help()
	else:
		outputUuidString=uuid.uuid4()
		print(outputUuidString)
'''