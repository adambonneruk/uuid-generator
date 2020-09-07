'''
Functions in this module are independenant of the unique/uuid-generator function that calls them.
Therefore there is the asumption they could work in other scenarios too.
'''

import re

def is_fqdn(hostname):
	'''
	FQDNs contain an empty element to the right of the TLD that signifies the unnamed domain root zone, and thus a
	trailing period follows the TLD "www.adambonner.co.uk.". However, today’s software (including internet browsers)
	usually processes the trailing period for us. The unnamed domain root zone essentially represents the internet.
	'''
	# if there is a trailing dot, remove it:
	if hostname[-1] == ".": # [-1] means last/ultimate element [-2] would be penultimate
		hostname = hostname[:-1] # [:-1] is array minus the last element

	# check length, and re pattern, if neither apply then True
	if len(hostname) > 253: #length/253: https://stackoverflow.com/questions/32290167/what-is-the-maximum-length-of-a-dns-name
		return False
	elif not re.search(r"^(?:(?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,63}$",hostname.lower()): #regex buddy: dns, international, strict
		return False
	else:
		return True

def is_oid(oid):
	print(r"^(?=.{0,64}$).*^([1-9][\d]*([\.][1-9][\d]*)*)$")
	return False

'''
last item of array
some_list = [1, 2, 3]
some_list[-1] = 5 # Set the last element
some_list[-2] = 3 # Set the second to last element
some_list
[1, 3, 5]

array minus 1
In [1]: [1, 2, 3, 4][:-1]
Out[1]: [1, 2, 3]
In [2]: "Hello"[:-1]
Out[2]: "Hell"
first item would be [1:]

a[start:end]
a[1:2]
[2]
a[start:]
a[1:]
[2, 3, 4, 5, 6]
'''
