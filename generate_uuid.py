"""Functions in this module are independenant of the unique function that calls them.
Therefore there is the asumption they could work in other scenarios too."""
import uuid

def uuid_0():
    """returns a special nil uuid"""
    return "00000000-0000-0000-0000-000000000000"

def uuid_1():
    """returns version 1 (datetime + mac address) uuid"""
    return str(uuid.uuid1())

def uuid_3(namespace, name):
    """returns version 3 (sha1 ns and name) uuid"""
    if namespace == "dns":
        uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_DNS, name))
    elif namespace == "url":
        uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_URL, name))
    elif namespace == "oid":
        uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_OID, name))
    elif namespace == "x500":
        uuid3_string = str(uuid.uuid3(uuid.NAMESPACE_X500, name))

    return uuid3_string

def uuid_4():
    """returns version 4 (random data) uuid"""
    return str(uuid.uuid4())

def uuid_5(namespace, name):
    """returns version 5 (sha1 ns and name) uuid"""
    if namespace == "dns":
        uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_DNS, name))
    elif namespace == "url":
        uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_URL, name))
    elif namespace == "oid":
        uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_OID, name))
    elif namespace == "x500":
        uuid5_string = str(uuid.uuid5(uuid.NAMESPACE_X500, name))

    return uuid5_string

def generate_uuid(version=4, urn_flag=False, namespace="dns", name="example.com", upper_flag=False):
    """Generate UUID passing in a number of flags for the configuration of the output string"""

    if version == 0:
        uuid_string = uuid_0()
    elif version == 1:
        uuid_string = uuid_1()
    elif version == 3:
        uuid_string = uuid_3(namespace, name)
    elif version == 4:
        uuid_string = uuid_4()
    elif version == 5:
        uuid_string = uuid_5(namespace, name)

    if upper_flag:
        uuid_string = uuid_string.upper()

    if urn_flag:
        uuid_string = "urn:uuid:" + uuid_string

    return uuid_string
