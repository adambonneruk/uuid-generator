import os
import sys
import re
import argparse
import logging
import uuid

from valid import is_fqdn
from valid import is_url
from valid import is_oid
from valid import is_x500

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
parser.add_argument("-s","--ns","--namespace",type=str,default="",dest="namespace",metavar="<NAMESPACE>",help="?")
parser.add_argument("-n","--name",type=str,default="",dest="name",metavar="<URL_OR_FQDN_NAME>",help="?")
parser.add_argument("-u","--urn",dest="urn_flag",action="store_true",default=False,help="?")
parser.add_argument("-U","--uppercase",dest="upper_flag",action="store_true",default=False,help="?")
args = parser.parse_args()

#sanitise input
args.namespace = args.namespace.lower()

logging.debug("\nOutput default or given settings")
logging.debug("\tVersion: " + str(args.version))
logging.debug("\tCount: " + str(args.count))
logging.debug("\tNamespace: " + str(args.namespace))
logging.debug("\tName: " + str(args.name))
logging.debug("\tURN Mode: " + str(args.urn_flag))
logging.debug("\tUppercase Mode: " + str(args.upper_flag))

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
	logging.debug("\tVersion " + str(args.version) + " Namespace and Name Checks")

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
		parser.error("valid namespace required for version " + str(args.version) + " uuids (dns, url, oid, or x500)")

	if str(args.name) == "":
		parser.error("name (e.g. url or fqdn) required for version " + str(args.version) + " uuids")
	else:
		logging.debug("\t\tName Entered")
		if str(args.namespace).upper() == "DNS":
			if is_fqdn(args.name):
				logging.debug("\t\tValid FQDN")
			else:
				parser.error("specified name for uuid v" + str(args.version) + " namespace is not a fqdn")
		elif str(args.namespace).upper() == "URL":
			if is_url(args.name):
				logging.debug("\t\tValid URL")
			else:
				parser.error("specified name for uuid v" + str(args.version) + " namespace is not a valid url")
		elif str(args.namespace).upper() == "OID":
			if is_oid(args.name):
				logging.debug("\t\tValid OID")
			else:
				parser.error("specified name for uuid v" + str(args.version) + " namespace is not an oid")
		elif str(args.namespace).upper() == "X500":
			if is_x500(args.name):
				logging.debug("\t\tValid X500 DN")
			else:
				parser.error("specified name for uuid v" + str(args.version) + " namespace is not an x500 dn")


else: #not v3/5 so v0/1/4
	if (str(args.namespace) != "" or str(args.name) != ""):
		parser.error("name and/or namespace not required/valid for UUID v1, v4 or nil (v0)")

def generate_uuids(version=4,quantity=1,urn_flag=False,namespace="dns",name="example.com",upper_flag=False):
	i = 1
	for i in range(i,quantity+1):

		if version == 0:
			uuidString = "00000000-0000-0000-0000-000000000000"
		elif version == 1:
			uuidString = str(uuid.uuid1())
		elif version == 4:
			uuidString = str(uuid.uuid4())
		elif version == 3:
			if namespace == "dns":
				uuidString = str(uuid.uuid3(uuid.NAMESPACE_DNS, name))
			elif namespace == "url":
				uuidString = str(uuid.uuid3(uuid.NAMESPACE_URL, name))
			elif namespace == "oid":
				uuidString = str(uuid.uuid3(uuid.NAMESPACE_OID, name))
			elif namespace == "x500":
				uuidString =str(uuid.uuid3(uuid.NAMESPACE_X500, name))
		elif version == 5:
			if namespace == "dns":
				uuidString = str(uuid.uuid5(uuid.NAMESPACE_DNS, name))
			elif namespace == "url":
				uuidString = str(uuid.uuid5(uuid.NAMESPACE_URL, name))
			elif namespace == "oid":
				uuidString = str(uuid.uuid5(uuid.NAMESPACE_OID, name))
			elif namespace == "x500":
				uuidString = str(uuid.uuid5(uuid.NAMESPACE_X500, name))

		if upper_flag: # == True
			uuidString = uuidString.upper()
		if urn_flag: # == True
			uuidString = "urn:uuid:" + uuidString

		print(uuidString)

logging.debug("\nUUIDs:")
generate_uuids(args.version,args.count,args.urn_flag,args.namespace,args.name,args.upper_flag)
