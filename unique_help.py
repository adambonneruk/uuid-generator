import sys

def help():
	print("Usage: unique.(py|exe) [-n <NUMBER_OF_UUIDS>] [-v <VERSION_OF_UUIDS>]")
	print("")
	print("Generate a number of version-specific UUIDs")
	print("")
	print("Supported Switches/Arguments.")
	print("  -c, --count\t specify the number of output UUIDs (1-65536)")
	print("  -v, --version\t specify which version the output UUIDs should be (1, 2, 3, or 4)")
	print("      --help\t display this help message")
	print("")
	print("Usage Examples:")
	print("  Generate 1 UUIDv4 (default behaviour)")
	print("\tunique")
	print("")
	print("  Generate 25 UUIDv4")
	print("\tunique -c 25 -v 4")
	print("")
	print("  Generate 100 UUIDv3")
	print("\tunique -c 100 -v 3")
	print("")
	print("")
	print("Adam Bonner, 2020, https://github.com/adambonneruk/uuid-generator")
	print("Python %s\n" % (sys.version,))
