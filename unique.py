import os
import sys
import re
import argparse
import logging

from generate import generate
from valid import isValidHostname

debug = True
if debug:
	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
	os.system("cls")
	logging.debug("DEBUG MODE ACTIVE")
	logging.debug(str(sys.argv))

logging.debug("\nConfigure Arguments")
parser = argparse.ArgumentParser(description="Generate a number of version specific UUIDs.")
parser.add_argument("-v","--version",type=int,default=4,dest="version",metavar="<UUID_VERSION>",help="?")
parser.add_argument("-c","--count",type=int,default=1,dest="count",metavar="<COUNT_OF_UUIDS>",help="?")
parser.add_argument("-s","--namespace",type=str,default="",dest="namespace",metavar="<NAMESPACE>",help="?")
parser.add_argument("-n","--name",type=str,default="",dest="name",metavar="<URL_OR_FQDN_NAME>",help="?")
parser.add_argument("-u","--urn",dest="urnFlag",action="store_const",const=True,default=False,help="?")
args = parser.parse_args()

logging.debug("\nOutput default or given settings")
logging.debug("\tVersion: " + str(args.version))
logging.debug("\tCount: " + str(args.count))
logging.debug("\tNamespace: " + str(args.namespace))
logging.debug("\tName: " + str(args.name))
logging.debug("\tURN Mode: " + str(args.urnFlag))

logging.debug("\nCheck settings are valid")
if re.search(r"^[01345]$",str(args.version)):
	logging.debug("\tVerion OK")
else:
	parser.error("not a valid uuid version (0, 1, 3, 4, 5)")

if (int(args.count) >= 1 and int(args.count) <= 65536):
	logging.debug("\tCount OK")
else:
	parser.error("count value out of limits (1 - 65536)")

if (str(args.version) == "3" or str(args.version) == "5"):
	logging.debug("\tVersion 3/5 Namespace and Name Checks")

	'''
		uuid.NAMESPACE_DNS
			When this namespace is specified, the name string is a fully-qualified domain name.
		uuid.NAMESPACE_URL
			When this namespace is specified, the name string is a URL.
		uuid.NAMESPACE_OID
			When this namespace is specified, the name string is an ISO OID.
		uuid.NAMESPACE_X500
			When this namespace is specified, the name string is an X.500 DN in DER or a text output format
	'''
	if re.search(r"^(DNS|URL|OID|X500)$",str(args.namespace).upper()):
		logging.debug("\t\tNamespace OK")
	else:
		parser.error("namespace required for version 3 and 5 uuids")

	if str(args.name) == "":
		parser.error("name (e.g. url or fqdn) required for version 3 and 5 uuids")
	else:
		logging.debug("\t\tName Entered")
		if str(args.namespace).upper() == "DNS":
			pass
		elif str(args.namespace).upper() == "URL":
			pass
		elif str(args.namespace).upper() == "OID":
			pass
		elif str(args.namespace).upper() == "X500":
			pass

print("UUID STRING HERE :-)")
