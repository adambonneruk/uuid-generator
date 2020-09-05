import uuid
import sys

from unique_help import help

if len(sys.argv) == 1: # default bahviour, just generate a single UUIdv4 (no arguments)
	outputUuidString=uuid.uuid4()
	print(outputUuidString)
else:
	if sys.argv[1] == '--help':
		help()
	else:
		outputUuidString=uuid.uuid4()
		print(outputUuidString)
