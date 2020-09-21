'''
Functions in this module are independenant of the unique/uuid-generator function that calls them.
Therefore there is the asumption they could work in other scenarios too.
'''
import re

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
