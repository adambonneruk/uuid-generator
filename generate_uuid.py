'''
Functions in this module are independenant of the unique function that calls them.
Therefore there is the asumption they could work in other scenarios too.
'''
import uuid

def generate_uuid(version=4, urn_flag=False, namespace="dns", name="example.com", upper_flag=False):
    """Generate UUID passing in a number of flags for the configuration of the output string"""
    if version == 0:
        uuid_string = "00000000-0000-0000-0000-000000000000"

    elif version == 1:
        uuid_string = str(uuid.uuid1())

    elif version == 4:
        uuid_string = str(uuid.uuid4())

    elif version == 3:
        if namespace == "dns":
            uuid_string = str(uuid.uuid3(uuid.NAMESPACE_DNS, name))
        elif namespace == "url":
            uuid_string = str(uuid.uuid3(uuid.NAMESPACE_URL, name))
        elif namespace == "oid":
            uuid_string = str(uuid.uuid3(uuid.NAMESPACE_OID, name))
        elif namespace == "x500":
            uuid_string = str(uuid.uuid3(uuid.NAMESPACE_X500, name))

    elif version == 5:
        if namespace == "dns":
            uuid_string = str(uuid.uuid5(uuid.NAMESPACE_DNS, name))
        elif namespace == "url":
            uuid_string = str(uuid.uuid5(uuid.NAMESPACE_URL, name))
        elif namespace == "oid":
            uuid_string = str(uuid.uuid5(uuid.NAMESPACE_OID, name))
        elif namespace == "x500":
            uuid_string = str(uuid.uuid5(uuid.NAMESPACE_X500, name))

    if upper_flag: # == True
        uuid_string = uuid_string.upper()

    if urn_flag: # == True
        uuid_string = "urn:uuid:" + uuid_string

    return uuid_string
