from valid import isValidHostname

hostname = "pyTHon.org."
print(hostname.lower())
if isValidHostname(hostname):
	print("yup, true")
else:
	print("nope, false")