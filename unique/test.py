import sys
from unique import Decode

tester = Decode(sys.argv[1])
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
