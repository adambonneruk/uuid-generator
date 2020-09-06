import re

def isValidHostname(hostname):
	if (len(hostname) <= 253 #length/253: https://stackoverflow.com/questions/32290167/what-is-the-maximum-length-of-a-dns-name
		and re.search(r"^(?:(?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,63}$",hostname[:-1].lower()) #regex buddy
	):
		return True
	else:
		return False

''' last item of array
some_list = [1, 2, 3]
some_list[-1] = 5 # Set the last element
some_list[-2] = 3 # Set the second to last element
some_list
[1, 3, 5]
'''

'''array minus 1
In [1]: [1, 2, 3, 4][:-1]
Out[1]: [1, 2, 3]
In [2]: "Hello"[:-1]
Out[2]: "Hell"
first item would be [1:]

a[start:end]
>>> a[1:2]
[2]
a[start:]
>>> a[1:]
[2, 3, 4, 5, 6]
'''

#^(?=.{0,64}$).*^([1-9][\d]*([\.][1-9][\d]*)*)$