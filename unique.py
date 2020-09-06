import sys
import re
import argparse

from help import help
from generate import generate
from valid import isValidHostname

import os
os.system("cls")
print("-------------------------------------")
print(str(sys.argv))

parser = argparse.ArgumentParser(description="Generate a number of version specific UUIDs.")

# Optional Arguments
parser.add_argument("-v","--version"
	,type=int,default = 4
	,dest="version"
	,metavar="<UUID_VERSION>"
	,help="?"
)
parser.add_argument("-c","--count"
	,type=int,default = 1
	,dest="count"
	,metavar="<COUNT_OF_UUIDS>"
	,help="?"
)
parser.add_argument("-n","--namespace"
	,type=str,default = ""
	,dest="namespace"
	,metavar="<NAMESPACE>"
	,help="?"
)
parser.add_argument("-s","--name"
	,type=str,default = ""
	,dest="name"
	,metavar="<URL_OR_FQDN_NAME>"
	,help="?"
)
# Option Flags (True/False)
parser.add_argument("-u","--urn"
	,dest="urnFlag"
	,action="store_const"
	,const=True,default=False
	,help="?"
)

args = parser.parse_args()

print("-------------------------------------")
print("Version: " + str(args.version))
print("Count: " + str(args.count))
print("Namespace: " + str(args.namespace))
print("Name: " + str(args.name))
print("URN Mode: " + str(args.urnFlag))

print("-------------------------------------")
if re.search(r"^[01345]$",str(args.version)):
	print("version ok")
else:
	parser.error("not a valid uuid version (0, 1, 3, 4, 5)")

if (int(args.count) >= 1 and int(args.count) <= 65536):
	print("count ok")
else:
	parser.error("count value out of limits (1 - 65536)")

print("-------------------------------------")
if (str(args.version) == "3" or str(args.version) == "5"):
	print(str(args.namespace) + "-")
	if str(args.namespace) == "":
		parser.error("namespace required for version 3 and 5 uuids")
	# check for valid name
		print("this")
	else:
		print("that")
else:
	# throw error is ns or n are passed in
	print("adam")	




#  if not args.two:
#        if args.three is None or args.four is None:
#            parser.error('without -2, *both* -3 <a> *and* -4 <b> are required')


"""

# Boolean flag (does not accept input data), with default value
parser.add_argument("-a1", action="store_true", default=False)

# Cast input to integer, with a default value
parser.add_argument("-a2", type=int, default=0)

# Provide long form name as well (maps to "argument3" not "a3")
parser.add_argument("-a3", "--argument3", type=str)

# Make argument mandatory
parser.add_argument("-a4", required=True)

# Retur the input via different parameter name
parser.add_argument("-a5", "--argument5", dest="my_argument")

args = parser.parse_args()
print(args.a1)
print(args.a2)
print(args.argument3)
print(args.a4)
print(args.my_argument)
"""