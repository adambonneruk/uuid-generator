import uuid
import base64
import codecs
from math import log

#uuid as formatted string
s = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
print("s: "+str(s))

print("") #################################################################

#uuid as hex
h = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org').hex
h = "4000a000000000000bff"
print("h: "+str(h))

#uuid as int
#i = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org').int
i = 10
print("i: "+str(i))

print("") #################################################################

#h as i (j)
j = int(h,16)
print("j: "+str(j))

#i as h (k)
k = hex(i)
print("k: "+str(k))

print("") #################################################################

def bytes_needed(n):
	if n == 0:
		return 1
	return int(log(n, 256)) + 1

n = bytes_needed(i)
print("n: "+str(n))

print("") #################################################################

#uuid in hex as binary
b = codecs.decode(h,'hex')
print("b: "+str(b))

#uuid in bin as hex
u_hex = codecs.encode(b,'hex')
x = str(u_hex)[2:-1]
print("x: " + x)

#uuid in bin as base64
u_b64 = codecs.encode(b,'base64')
y = str(u_b64)[2:-3]
print("y: " + y)

print("") #################################################################

b64_as_bin = codecs.decode(u_b64,'base64')
print("p: " + str(b64_as_bin))
bin_as_hex = codecs.encode(b64_as_bin,'hex')
print("q: " + str(bin_as_hex))

print("") ################################################################# 886313e13b8a53729b900c9aee199e5d

z = uuid.UUID(str(bin_as_hex)[2:-1].zfill(32))
print("z: " + str(z))


#step3 = str(step2)[2:-1]
#print ("step3: " + step3)
#btt64 = uuid.UUID(step3)
#print(btt64)

'''if btt64 == s:
	print("working")
else:
	print("not working")
'''
# wpsWLdLt9nscn2jbTD3uxe
# iGMT4TuKU3KbkAya7hmeXQ==