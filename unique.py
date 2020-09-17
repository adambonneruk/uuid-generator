"""Generate a Unique UUID"""
import sys
import argparse
import logging

from valid import is_uuid_version, is_reasonable_quantity, is_uuid_namespace, is_uuid_ns_name
from generate_uuid import generate_uuid

#Enabled/Disable Debug Mode
DEBUGMODE = False
if DEBUGMODE:
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.debug("DEBUG MODE ACTIVE")
    logging.debug(str(sys.argv))

#Configure Arguments
logging.debug("\nConfigure Arguments")
parser = argparse.ArgumentParser(description="Generate a number of version specific UUIDs.")
parser.add_argument("-v", "--version",
                    type=int,
                    default=4,
                    dest="version",
                    metavar="<VERSION>",
                    help="Specify output UUID version (0, 1, 3, 4, or 5)"
                    )
parser.add_argument("-q", "--quantity",
                    type=int,
                    default=1,
                    dest="quantity",
                    metavar="<QUANTITY>",
                    help="Specify output quanitity (1 - 65536)"
                    )
parser.add_argument("--ns", "--namespace",
                    type=lambda s: s.lower(),
                    default="",
                    dest="namespace",
                    metavar="<NAMESPACE>",
                    help="UUID v3 or v5 namespace"
                    )
parser.add_argument("-n", "--name",
                    type=str,
                    default="",
                    dest="name",
                    metavar="<NAME>",
                    help="Specify UUID v3 or v4 name"
                    )
parser.add_argument("-u", "--urn",
                    dest="urn_flag",
                    action="store_true",
                    default=False,
                    help="Specify URN standard prefix"
                    )
parser.add_argument("-U", "--uppercase",
                    dest="upper_flag",
                    action="store_true",
                    default=False,
                    help="Non-standard uppercase UUID string"
                    )
args = parser.parse_args()

#Argument Validation
logging.debug("\nValidate Arguments")
#Quanitity Check
logging.debug("\n\tQuantity: %s", str(args.quantity))
if not is_reasonable_quantity(args.quantity):
    parser.error("Not a Valid Quantity")
else:
    logging.debug("\tQuantity OK")

#URN Check
logging.debug("\n\tURN Mode: %s", str(args.urn_flag))

#Uppercase Check
logging.debug("\n\tUppercase Mode: %s", str(args.upper_flag))

#Version Check
logging.debug("\n\tVersion: %s", str(args.version))
if not is_uuid_version(args.version):
    parser.error("Not a Valid UUID Version")
else:
    logging.debug("\tVersion OK")

    #Versions 0, 1, and 4
    if (str(args.version) == "0" or str(args.version) == "1" or str(args.version) == "4"):
        logging.debug("\tNamespace and Name: Not Required")
        if str(args.namespace) != "":
            parser.error("Namespace not required for Version " + str(args.version) + " UUID")
        if str(args.name) != "":
            parser.error("Name not required for Version " + str(args.version) + " UUID")

    #Versions 3 and 5
    elif (str(args.version) == "3" or str(args.version) == "5"):
        logging.debug("\tNamespace and Name: Required")

        #Namespace Checking
        logging.debug("\n\tNamespace: %s", str(args.namespace))
        if str(args.namespace) == "":
            parser.error("Namespace required for Version " + str(args.version) + " UUID")
        elif not is_uuid_namespace(args.namespace):
            parser.error("Not a Valid Namespace")
        else:
            logging.debug("\tNamespace OK")

        #Namespace & Name Checking
        logging.debug("\n\tName: %s", str(args.name))
        if str(args.name) == "":
            parser.error("Name required for Version " + str(args.version) + " UUID")
        elif not is_uuid_ns_name(args.namespace, args.name):
            parser.error("Not a Valid Name for " + str(args.namespace).upper() + " Namespace")
        else:
            logging.debug("\tName OK")

    else:
        pass

#Print UUID "q" times
logging.debug("\nUUIDs:")
for i in range(0, args.quantity):
    output_uuid = generate_uuid(args.version, # pylint: disable=C0103
                                args.urn_flag,
                                args.namespace,
                                args.name,
                                args.upper_flag
                                )

    print(output_uuid)
