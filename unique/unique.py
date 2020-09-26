"""Generate or Decode a Universally Unique ID (CLI and Object)"""
import uuid
import codecs
import re
import argparse
from datetime import datetime
from datetime import timedelta
from ulid import Ulid

def is_uuid_version(version):
    '''version (int) check, should be 0, 1, 3, 4, or 5'''
    return bool(re.search(r"^[01345]$", str(version)))

def is_reasonable_quantity(quantity):
    '''quantity (int) check, should be 1 - 65535'''
    return bool(quantity >= 1 and quantity <= 65536)

def is_uuid_namespace(namespace):
    '''namespace (str) check, should be dns|url|oid|x500'''
    return bool(re.search(r"^(dns|url|oid|x500)$", str(namespace)))

def is_uuid_ns_name(namespace, name):
    '''name (str) check for given namespace (str)'''
    return bool(
        (namespace == "dns" and is_fqdn(name))
        or (namespace == "url" and is_url(name))
        or (namespace == "oid" and is_oid(name))
        or (namespace == "x500" and is_x500(name))
    )

def is_fqdn(hostname):
    '''
    FQDNs contain an empty element to the right of the TLD that signifies the unnamed domain root
    zone, and thus a trailing period follows the TLD "www.adambonner.co.uk.". However, today’s
    software (including internet browsers) usually processes the trailing period for us. The
    unnamed domain root zone essentially represents the internet.

    Domain name (internationalized, strict)
    Allow internationalized domains using punycode notation, as well as regular domain names.
    Use lookahead to check that each part of the domain name is 63 characters or less.
    '''
    # if there is a trailing dot, remove it:
    if hostname[-1] == ".":
        hostname = hostname[:-1]

    #lowercase hostname for purpose of the check
    hostname = hostname.lower()

    # check length, and re pattern, if neither apply then True
    return bool(
        len(hostname) <= 253
        and re.search(
            r'^(?:(?=[a-z0-9-]{1,63}\.)'
            r'(xn--)?[a-z0-9]+(?:-[a-z0-9]+)*\.)+'
            r'[a-z]{2,63}$', hostname)
    )

def is_oid(oid):
    '''
    An OID corresponds to a node in the "OID tree" or hierarchy, Each node in the tree is
    represented by a series of integers separated by periods, corresponding to the path from the
    root through the series of ancestor nodes, to the node.
    '''
    return bool(re.search(r"^(?=.{0,64}$).*^([1-9][\d]*([\.][1-9][\d]*)*)$", oid))

def is_url(url):
    '''
    A Uniform Resource Locator (URL), colloquially termed a web address, is a reference to a web
    resource that specifies its location on a computer network and a mechanism for retrieving it.
    '''
    #lowercase for check
    url = url.lower()

    url_regex = re.compile(
        r'^(?:http|ftp)s?://' #http or https
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #dn
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' #or ip
        r'(?::\d+)?' #optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return bool(url_regex.match(url))

def is_x500(x500):
    '''
    X.500 Distinguished Names are used to identify entities, such as those which are named by the
    subject and issuer (signer) fields of X.509 certificates. keytool supports the following
    subparts:

    commonName - common name of a person, e.g., "Susan Jones"
    organizationUnit - small organization (e.g, department or division) name, e.g., "Purchasing"
    organizationName - large organization name, e.g., "ABCSystems, Inc."
    localityName - locality (city) name, e.g., "Palo Alto"
    stateName - state or province name, e.g., "California"
    country - two-letter country code, e.g., "CH"
    '''
    x500ns_regex = re.compile(
        r'^(?:[A-Za-z][\w-]*|\d+(?:\.\d+)*)='#Attribure Type
        r'(?:#(?:[\dA-Fa-f]{2})+' #Attribute Value: A Hex String
        r'|(?:[^,=\+<>#;\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*' #Attribute Value: Escaped String
        r'|"(?:[^\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*")' #Attribute Value: Quoted String
        r'(?:\+(?:[A-Za-z][\w-]*|\d+(?:\.\d+)*)='
        r'(?:#(?:[\dA-Fa-f]{2})+'
        r'|(?:[^,=\+<>#;\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*'
        r'|"(?:[^\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*"))*'
        r'(?:,(?:[A-Za-z][\w-]*|\d+(?:\.\d+)*)='
        r'(?:#(?:[\dA-Fa-f]{2})+'
        r'|(?:[^,=\+<>#;\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*'
        r'|"(?:[^\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*")'
        r'(?:\+(?:[A-Za-z][\w-]*|\d+(?:\.\d+)*)='
        r'(?:#(?:[\dA-Fa-f]{2})+'
        r'|(?:[^,=\+<>#;\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*'
        r'|"(?:[^\\"]|\\[,=\+<>#;\\"]|\\[\dA-Fa-f]{2})*"))*)*$')

    return bool(x500ns_regex.match(x500))

class Unique:
    """unique is a unique number with specific properties"""
    def __init__(self, version=4, namespace=None, name=None):
        if version in [0, 1, 4]:
            pass
        elif version in [3, 5]:
            if is_uuid_namespace(namespace) and is_uuid_ns_name(namespace, name):
                pass
            else:
                raise ValueError("Namespace or Name Invalid")
        else:
            raise ValueError("Not a Valid UUID Version")

        # Object Attributes
        self._version = version
        self._namespace = namespace
        self._name = name
        self.__generate_uuid()

    # Property Getters
    @property
    def version(self):
        """returns the version"""
        return self._version

    @property
    def namespace(self):
        """returns the namespace"""
        return self._namespace

    @property
    def name(self):
        """returns the name"""
        return self._name

    # Private Methods
    def __generate_uuid(self):
        if self._version == 0:
            self._uuid = "00000000-0000-0000-0000-000000000000"
        if self._version == 1:
            self._uuid = str(uuid.uuid1())
        if self._version == 3:
            self._uuid = self.__uuid3()
        if self._version == 4:
            self._uuid = str(uuid.uuid4())
        if self._version == 5:
            self._uuid = self.__uuid5()

    def __uuid5(self):
        """returns version 5 (sha1 ns and name) uuid"""
        if self._namespace == "dns":
            uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_DNS, self._name))
        elif self._namespace == "url":
            uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_URL, self._name))
        elif self._namespace == "oid":
            uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_OID, self._name))
        elif self._namespace == "x500":
            uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_X500, self._name))
        return uuid5_string

    def __uuid3(self):
        """returns version 3 (md5 ns and name) uuid"""
        if self._namespace == "dns":
            uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_DNS, self._name))
        elif self._namespace == "url":
            uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_URL, self._name))
        elif self._namespace == "oid":
            uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_OID, self._name))
        elif self._namespace == "x500":
            uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_X500, self._name))
        return uuid3_string

    # Public Methods
    def __str__(self):
        return str(self._uuid)

    def encode(self):
        """convert dashed-hexidecimal to base64 uuid"""
        hex_uuid = uuid.UUID(self._uuid).hex
        bin_uuid = codecs.decode(hex_uuid, "hex")
        b64_uuid = codecs.encode(bin_uuid, "base64")
        output_uuid = str(b64_uuid)[2:-3]
        return output_uuid

    def prefix(self):
        """prefix uuid with rfc-4122 urn string"""
        return "urn:uuid:" + self._uuid

    def hex(self):
        """return uuid as hexadecimal (without dashes)"""
        hex_uuid = uuid.UUID(self._uuid).hex
        return hex_uuid

    def int(self):
        """return uuid as integer"""
        int_uuid = uuid.UUID(self._uuid).int
        return int_uuid

    def upper(self):
        """return uuid as non-standard uppercase letters"""
        return self._uuid.upper()

    def datetime(self):
        """extract the datetime from a UUIDv1 string"""
        if self._version == 1:
            #https://stackoverflow.com/questions/3795554/extract-the-time-from-a-uuid-v1-in-python
            dttm = datetime(1582, 10, 15) + timedelta(microseconds=uuid.UUID(self._uuid).time//10)
        else:
            dttm = "n/a"
        return dttm

    def mac_address(self):
        """extract the mac address from a UUIDv1 using string manipulation"""
        if self._version == 1:
            mac_plain = self._uuid[-12:]
            mac_formatted = '-'.join(mac_plain[i:i + 2] for i in range(0, 12, 2))
        else:
            mac_formatted = "n/a"
        return mac_formatted

    def version_desc(self):
        """pretty decription of each known uuid version, otherwise: unknown"""
        if self._version == 0:
            description = "Special Case: DCE 1.1 Nil UUID"
        elif self._version == 1:
            description = "Time and Node Based UUID"
        elif self._version == 3:
            description = "Namespace (MD5) Based UUID"
        elif self._version == 4:
            description = "Random Data Based UUID"
        elif self._version == 5:
            description = "Namesapce (SHA-1) Based UUID"
        else:
            description = "Unknown"
        return description

class Decode(Unique):
    """decode is a Unique with a number of informational properties"""
    def __init__(self, incoming):
        super().__init__()
        #fail safe
        self._version = 9
        self._namespace = ""
        self._name = ""

        #new property varibles
        self._incoming = incoming
        self.__is_supported_regex()
        self._version = self.__parse_version()

    # Property Getters
    @property
    def version(self): #override Unique() getter
        """returns the version"""
        return self._version

    @property
    def namespace(self): #override Unique() getter
        """returns the namespace"""
        if self._version in [0, 1, 4]:
            namespace = None
        elif self._version in [3, 5]:
            namespace = "Unknown"
        else:
            namespace = "Undetermined"
        return namespace

    @property
    def name(self): #override Unique() getter
        """returns the name"""
        if self._version in [0, 1, 4]:
            name = None
        elif self._version in [3, 5]:
            name = "Unknown"
        else:
            name = "Undetermined"
        return name

    @property
    def input_string(self):
        """returns the input string"""
        return self._incoming

    @property
    def input_type(self):
        """returns the input type"""
        return self._input_type

    # Private Methods
    def __is_supported_regex(self):
        if re.search(r"[a-zA-Z0-9\+\/]{22}==", self._incoming):
            self._uuid = self.__decode_b64()
            self._input_type = "Base64"
        elif re.search(r"[0-9a-f]{32}", self._incoming.lower()):
            self._uuid = self.__decode_hex()
            self._input_type = "Hexadecimal"
        elif re.search(r"urn:uuid:"
                       r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", self._incoming):
            print("urnprefix")
            self._input_type = "URN Prefix"
        elif re.search(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", self._incoming.lower()):
            self._uuid = self._incoming.lower()
            self._input_type = "Plain Text"
        else:
            raise ValueError("not a valid/supported uuid format")

    def __decode_b64(self):
        """convert base64 to dashed-hexadecimal uuid"""
        b64_uuid = self._incoming.encode("ascii")
        bin_uuid = codecs.decode(b64_uuid, 'base64')
        hex_uuid = codecs.encode(bin_uuid, 'hex')
        str_uuid = uuid.UUID(str(hex_uuid)[2:-1].zfill(32))
        output_uuid = str(str_uuid)
        return output_uuid

    def __decode_hex(self):
        """convert hex to dashed-hexadecimal uuid"""
        str_uuid = uuid.UUID(self._incoming)
        output_uuid = str(str_uuid)
        return output_uuid

    def __parse_version(self):
        """grab the uuid version from the string"""
        return int(self._uuid[14:15], 16)

def uuid_generate(args, parser):
    """Validates severage inbound arguments then prints x number of UUIDs"""
    #Argument Validation
    if not is_reasonable_quantity(args.quantity):
        parser.error("Not a Valid Quantity")

    #Version Check
    if not is_uuid_version(args.version):
        parser.error("Not a Valid UUID Version")

    if args.version in [0, 1, 4] and (str(args.namespace) != "" or str(args.name) != ""):
        parser.error("Namespace/Name not required for Version " + str(args.version) + " UUID")

    if args.version in [3, 5]:
        if str(args.namespace) == "" or str(args.name) == "":
            parser.error("Namespace and Name required for Version " + str(args.version) + " UUID")
        elif not is_uuid_namespace(args.namespace):
            parser.error("Not a Valid Namespace")
        elif not is_uuid_ns_name(args.namespace, args.name):
            parser.error("Not a Valid Name for " + str(args.namespace).upper() + " Namespace")

    #Print UUID "--quantity" times
    for _ in range(0, args.quantity):
        myuuid = Unique(args.version, args.namespace, args.name)

        if args.upper_flag:
            print(myuuid.upper())
        elif args.urn_flag:
            print(myuuid.prefix())
        elif args.short_flag:
            print(myuuid.encode())
        else:
            print(myuuid)

def ulid_generate(args, parser):
    """Validates arguments then prints x number of ULIDs"""
    # Argument Validation
    if not is_reasonable_quantity(args.quantity):
        parser.error("Not a Valid Quantity")

    # Print ULID "--quantity" times
    for _ in range(0, args.quantity):
        myulid = Ulid()
        print(myulid)

def uuid_decode(args, parser):
    """validates incoming string and if a uuid and pretty prints or fully parses"""

    #Catch Non-Conformant UUID / Decode class has several RegEx checks in __is_supported_regex()
    try:
        tester = Decode(args.raw_uuid)
    except ValueError:
        parser.error("Not a Valid (Hex|Base64|Uppercase|Prefixed) UUID")

    # Pretty Print or Full Information?
    if args.full_info:
        print("Input String: \t" + str(tester.input_string))
        print("Input Type: \t" + str(tester.input_type))
        print("UUID:   \t" + str(tester))
        print("Version: \t" + str(tester.version))
        print("Description: \t" + str(tester.version_desc()))
        print("Namespace: \t" + str(tester.namespace))
        print("Name:   \t" + str(tester.name))
        print("Date & Time: \t" + str(tester.datetime()))
        print("MAC Address: \t" + str(tester.mac_address()))
        print("Base64: \t" + str(tester.encode()))
        print("URN Prefix: \t" + str(tester.prefix()))
        print("Hexadecimal: \t" + str(tester.hex()))
        print("Integer: \t" + str(tester.int()))
        print("Uppercase: \t" + str(tester.upper()))
    else:
        # Pretty Print the UUID (lowercase string with dashes/groups)
        print(tester)

def main():
    """Using Main to execute a CLI based UUID Generate/Decode tool"""
    # Default Parser
    parser = argparse.ArgumentParser(description="Generate or Decode a Universally Unique ID",
                                     epilog="Unique v5.0.0 | Adam Bonner | 2020",
                                     allow_abbrev=False) # fix: --help not --he
    parser.set_defaults(func=uuid_generate) #call uuid_generate() function

    # Default Parser (Mutually Exclusive Group)
    parser_meg = parser.add_mutually_exclusive_group()

    # Secondary "Decode()" Parser / Subparser
    subparsers = parser.add_subparsers(help='Pretty-print and display UUID information')
    decode = subparsers.add_parser('decode')
    decode.set_defaults(func=uuid_decode) #call uuid_decode() function
    ulid = subparsers.add_parser('ulid')
    ulid.set_defaults(func=ulid_generate) #call ulid_generate() function

    # Add Arguments - Main Parser
    parser.add_argument("-v", "--version", type=int, default=4, dest="version",
                        metavar="<VERSION>",
                        help="Specify output UUID version (0, 1, 3, 4, or 5)")
    parser.add_argument("-q", "--quantity", type=int, default=1, dest="quantity",
                        metavar="<QUANTITY>",
                        help="Specify output quantity (1 - 65536)")
    parser.add_argument("--ns", "--namespace", type=lambda s: s.lower(), default="",
                        dest="namespace", metavar="<NAMESPACE>",
                        help="UUID v3 or v5 namespace")
    parser.add_argument("-n", "--name", type=str, default="", dest="name",
                        metavar="<NAME>",
                        help="Specify UUID v3 or v5 name")

    # Add Arguments - Main Parser (MEG)
    parser_meg.add_argument("-u", "--urn", dest="urn_flag",
                            action="store_true", default=False,
                            help="Specify URN standard prefix")
    parser_meg.add_argument("-U", "--uppercase", dest="upper_flag",
                            action="store_true", default=False,
                            help="Non-standard uppercase UUID string")
    parser_meg.add_argument("-s", "--short", dest="short_flag",
                            action="store_true", default=False,
                            help="Shortened UUID using Base64 Encoding")

    # Add Arguments - Decode Subparser
    decode.add_argument('raw_uuid', type=str, metavar='UUID',
                        help='A valid (Hex|Base64|Uppercase|Prefixed) UUID string')
    decode.add_argument('-i', "--information", dest="full_info",
                        action="store_true", default=False,
                        help="Provide detailed information about decoded UUID")

    # Add Arguments - Decode Subparser
    ulid.add_argument("-q", "--quantity", type=int, default=1, dest="quantity",
                      metavar="<QUANTITY>",
                      help="Specify output quantity (1 - 65536)")

    # Store the ArgParse Arguments in a Varible named Args
    args = parser.parse_args()

    # Execute the request ArgParse Function
    args.func(args, parser)

if __name__ == "__main__":
    main()
