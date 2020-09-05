import sys
import re

from unique_help import help
from unique_generate import generate

if not re.search(r"--help",str(sys.argv)): ## display just help if "--help" argument found
	try:
		args = len(sys.argv) - 1 # number of arguments (minus the program itself)
		version = 4
		count = 1
		argumentError = False
		for i in range(1, args + 1): # 1 to the number of arguments

			if not re.search(r"^(-v|--version|-c|--count|\d+)$",sys.argv[i]):
				argumentError = True
			else:
				try:
					if re.search(r"^(-v|--version)$",sys.argv[i]):
						version = int(sys.argv[i+1])
					if re.search(r"^(-c|--count)$",sys.argv[i]):
						count = int(sys.argv[i+1])
				except:
					argumentError = True

		if argumentError == True :
			print("error: invalid argument(s)")
			quit(-1)

		elif re.search(r"^[^014]$",str(version)):
			print("error: uuid version incorrect")
			quit(-1)

		elif count < 1 or count > 65536:
			print("error: incorrect number (count) of outputs")
			quit(-1)

		else:
			generate(version,count)

	except:
		help()
		quit(-1)

else:
	help()
