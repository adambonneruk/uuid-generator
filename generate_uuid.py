import uuid

def generate_uuid(version=4,urn_flag=False,namespace="dns",name="example.com",upper_flag=False):
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

	return uuidString