# uuid-generator (in Python)
CLI-based Version 4 UUID Generator. Written in Python using Python 3.8.5. Executable created with pyinstaller 4.0

## Background
Sometimes you just need a nice random number for some purpose, what better than a UUID! I first worked on this problem back in May 2016. I need a random number generator and started learning about UUIDs. This tool started as a way to automatically generate 20 v4 UUIDs (the only random one not engineered to a set of hardware etc.) and has now been updated and released to demonstrate my Python skills; such as using modules, arguments, for loops, function parameter defaulting (as opposed to overloading) and regex. 

## Usage
```powershell
# single UUIDv4
>./unique.exe
f6c50e93-92ba-40af-a85e-bf466acf7b52

# five UUIDv4
>./unique.exe --count 5
32ec9ca1-2a84-40c9-afa4-f67a7a8c3156
039ee9f1-c5a0-4d85-805a-89b84974a6c7
b6a4587d-a3de-4e4c-8d84-a3fad6b14192
91bd7bf0-8b6e-46af-ad01-7f91ca66aa25
4085c90e-b195-40fb-b31e-e5faf76eb34a

# two UUIDv1
>./unique.exe --version 1 -c 7
6e75ec44-ef9b-11ea-aeea-e4b31802edf0
6e75ec45-ef9b-11ea-b621-e4b31802edf0

# single special nil UUID
>./unique.exe -c 1 -v 0
00000000-0000-0000-0000-000000000000

```
### Help File
Using the ```--help``` switch will trigger the help text
```
usage: unique.(py|exe) [-n <number_of_UUIDs>] [-v <version_of_UUIDs>]

generate a number of version-specific UUIDs

supported switches/arguments.
  -c, --count    specify the number of output UUIDs (1-65536)
  -v, --version  specify which version the output UUIDs should be (0, 1, or 4)
      --help     display this help message

usage examples:
  generate 1 UUIDv4 (default behaviour)
        unique

  generate 25 UUIDv4
        unique -c 25 -v 4

  generate 100 UUIDv1
        unique -c 100 -v 1
```

## [Wikipedia](https://https://en.wikipedia.org/wiki/Universally_unique_identifier) description of UUID:
A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems.

When generated according to the standard methods, UUIDs are, for practical purposes, unique. Their uniqueness does not depend on a central registration authority or coordination between the parties generating them, unlike most other numbering schemes. While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible. Thus, anyone can create a UUID and use it to identify something with near certainty that the identifier does not duplicate one that has already been, or will be, created to identify something else. Information labeled with UUIDs by independent parties can therefore be later combined into a single database or transmitted on the same channel, with a negligible probability of duplication.

### UUIDv0 / Nil UUID
The "nil" UUID, a special case, is the UUID 00000000-0000-0000-0000-000000000000; that is, all bits set to zero.

### [UUIDv1](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address))
rsion 1 concatenates the 48-bit MAC address of the "node" (that is, the computer generating the UUID), with a 60-bit timestamp, being the number of 100-nanosecond intervals since midnight 15 October 1582 Coordinated Universal Time (UTC), the date on which the Gregorian calendar was first adopted. RFC 4122 states that the time value rolls over around 3400 AD, depending on the algorithm used, which implies that the 60-bit timestamp is a signed quantity. 

### [UUIDv4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random))
A version 4 UUID is randomly generated. As in other UUIDs, 4 bits are used to indicate version 4, and 2 or 3 bits to indicate the variant (102 or 1102 for variants 1 and 2 respectively). Thus, for variant 1 (that is, most UUIDs) a random version-4 UUID will have 6 predetermined variant and version bits, leaving 122 bits for the randomly generated part, for a total of 2122, or 5.3×1036 (5.3 undecillion) possible version-4 variant-1 UUIDs. There are half as many possible version-4 variant-2 UUIDs (legacy GUIDs) because there is one less random bit available, 3 bits being consumed for the variant.

## Prerequisites
* Python 3 (3.8.5+)
  * sys
  * os
* PyInstaller (4.0+)

### Install Guide
```powershell
choco install python
# restart commandline for system path edits
pip install pyinstaller
```

## Note / Limitations
* currently only support UUIDv1 and UUIDv4 with the special "v0" nil UUID

## Future Ideas (braindump)
* Adding support for uuid namespaces, including UUIDv3 and UUIDv5

