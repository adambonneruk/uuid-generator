import sys
import re

from unique_help import help
from unique_generate import generate

###############################################################################
import os
os.system("cls")
###############################################################################

args = len(sys.argv) - 1 # number of arguments (minus the program itself)



if args == 0:
	generate()
elif args == 2:
	print("...two")
	if re.search(r"^(-v|--version)$",sys.argv[1]):
		generate(sys.argv[2],1)
	elif re.search(r"^(-c|--count)$",sys.argv[1]):
		generate(4,sys.argv[2])
	else:
		help()
elif args == 4:
	print("...four")
else:
	help()
