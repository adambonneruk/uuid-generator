# uuid-generator (in Python) ![](icon/32.png)
UUID generator tools. ```unique-gui.exe``` and ```unique.exe``` will UUIDs with a number of customisable options (via the menu bar or using the ```-v``` and ```-c``` switches can change the version and quantity of output UUIDs as required). This project builds on code originally developed in 2016; leveraging different python libraries to provide a comprehensive unix-like experience. Executables created with pyinstaller 4.0

## Background
Sometimes you just need a nice random number for your purpose, what better than a UUID! I first worked on this problem back in May 2016. I need a random number generator and started learning about UUIDs. This tool started as a way to automatically generate 20 v4 UUIDs (the only random one not engineered to a set of hardware etc.) and has now been updated and released to demonstrate my Python skills; using Tkinter (for the GUI) Modules, Arguments, Function/Parameter defaulting (as opposed to overloading), URI, OID, X.500 Distinguished Names and RegEx.

## UUID (from [Wikipedia](https://https://en.wikipedia.org/wiki/Universally_unique_identifier))
A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems. UUIDs are, for practical purposes, unique. Their uniqueness does not depend on a central registration authority or coordination between the parties generating them. While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible. Thus, anyone can create a UUID and use it to identify something with near certainty that the identifier does not duplicate one that has already been, or will be, created to identify something else. Information labe;led with UUIDs by independent parties can therefore be later combined into a single database or transmitted on the same channel, with a negligible probability of duplication.

>__Note:__ A Version 4 UUID is the default, safe and extremely random output of this tool.

### Further Reading:
* [URN / Uniform Resource Name](https://en.wikipedia.org/wiki/Uniform_Resource_Name), [URI / Uniform Resource Identifier
](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) and [URL / Uniform Resource Locator](https://en.wikipedia.org/wiki/URL)
* [OID / object identifier](https://en.wikipedia.org/wiki/Object_identifier)
* [X.500 Distinguished Names](https://www.ibm.com/support/knowledgecenter/en/SSYKE2_7.0.0/com.ibm.java.security.component.70.doc/security-component/keytoolDocs/x500dnames.html)
* [MAC Address](https://www.ibm.com/support/knowledgecenter/en/SSYKE2_7.0.0/com.ibm.java.security.component.70.doc/security-component/keytoolDocs/x500dnames.html)

## Usage (GUI: ```unique-gui.exe```)
Using the ```tkinter``` library, a gui is available to generate UUIDs for those not comfortable with the command line. Simple open/execute ```unique-gui.pyw```/```unique-gui.exe``` to be presented with the following grpahical interface:

![](screenshots/gui.png)

The following Menu options are availble:
* File
  * __New__: Clear-down the UUIDs in the current tool, ready for new generation
  * __Open__: Open a text (```.txt```) file, useful for appending UUIDs
  * __Save__: Save the current UUIDs to a text (```.txt```) file
* Generate UUIDs
  * __Version 0__: Generate a Nil UUID
  * __Version 1__: Generare a Version 1 (Datetime & MAC Address) UUID
  * __Version 3__: Generate a Version 3 (MD5, Namespace & Name-based) UUID
  * __Version 4__: Generate a Version 4 UUID (based on RNG)
  * __Version 5__: Generate a Version 5 (SHA-1, Namespace & Name-based) UUID
* Configuration
  * __Quantity__: Prompt to spefici number of UUIDs required (will be asked on first UUID creation)
  * __URN Prefix__: Yes/No Option for URN Prefix
  * __Uppercase__: Yes/No Option for Non-Standard Uppercase Output
  * __Set Namespace__: Set Namespace for Name (will be asked on first UUIDv3/5 creation)
  * __Set Name__: Set Hashable Input (will be asked on first UUIDv3/5 creation)
* Help
  * __About__: Opens a small about window with author/version information


## Usage (Command Line: ```unique.exe```)
```powershell
# UUIDv4
>./unique.exe
27fd1448-3c0d-4d73-94c4-9f16dd9e0c16

# 5 x UUIDv4
>./unique.exe -c 5
32ec9ca1-2a84-40c9-afa4-f67a7a8c3156
039ee9f1-c5a0-4d85-805a-89b84974a6c7
b6a4587d-a3de-4e4c-8d84-a3fad6b14192
91bd7bf0-8b6e-46af-ad01-7f91ca66aa25
4085c90e-b195-40fb-b31e-e5faf76eb34a

# 2 x UUIDv1 with URN prefix
>./unique.exe -v 1 -c 2 -u
urn:uuid:7ed04b31-f14c-11ea-ac52-e4b31802edf0
urn:uuid:7ed0c3d9-f14c-11ea-aabd-e4b31802edf0

# Special Nil UUID
>./unique.exe -c 1 -v 0
00000000-0000-0000-0000-000000000000

# UUIDv5 for "python.org" Fully qualified domain name
>./unique.exe -v 5 --ns dns -n "python.org"
886313e1-3b8a-5372-9b90-0c9aee199e5d

# Uppercase UUIDv3 for "http://adambonner.co.uk" URL with URN prefix
>./unique.exe -U -v 3 -n "http://adambonner.co.uk" --ns url -u
urn:uuid:1FDC56DF-BB86-3F0D-9356-8612ABA227FF

# Display Help
>./unique.exe --help
usage: unique.py [-h] [-v <UUID_VERSION>] [-c <COUNT_OF_UUIDS>] [-s <NAMESPACE>] [-n <URL_FQDN_OID_X500_NAME>] [-u] [-U]

Generate a number of version specific UUIDs.

optional arguments:
  -h, --help            show this help message and exit
  -v <UUID_VERSION>, --version <UUID_VERSION>
                        Specify UUID version: 0/nil, 1, 3, 4, or 5
  -c <COUNT_OF_UUIDS>, --count <COUNT_OF_UUIDS>
                        Specify number of output UUIDs (max. 65536)
  -s <NAMESPACE>, --ns <NAMESPACE>, --namespace <NAMESPACE>
                        UUID v3 or v5 namespace
  -n <URL_FQDN_OID_X500_NAME>, --name <URL_FQDN_OID_X500_NAME>
                        Specify UUID v3 or v4 name
  -u, --urn             Specify URN standard prefix
  -U, --uppercase       Non-standard uppercase UUID string

```

## Supported UUID Versions

Version | Switch        | Specifics                  | Additional Options (Bold = Mandatory)
--------|---------------|----------------------------|---------------------------------------------------------
0 / Nil | --version 0   | Special Nil UUID           | --count, --urn, --uppercase
1       | --version 1   | Datetime and MAC address   | --count, --urn, --uppercase
3       | --version 3   | Namespace & Name-based     | --count, --urn, --uppercase, __--namespace__, __--name__
4       | --version 4   | Random Data                | --count, --urn, --uppercase
5       | --version 5   | Namespace & Name-based     | --count, --urn, --uppercase, __--namespace__, __--name__

## Prerequisites
* Python 3 (3.8.5+)
  * os
  * sys
  * re
  * argparse
  * logging
  * uuid
  * tk (inc. messagebox & simpledialog)
* PyInstaller (4.0+)
* [Paint.net 4.2.13](https://www.getpaint.net)
* [IcoFX Portable (1.6.4 Rev 3)](https://portableapps.com/apps/graphics_pictures/icofx_portable)

### Install Guide
How to configure ```uuid-generator``` in your environment:
```powershell
choco install python -y
#restart after installing python
pip install pyinstaller
```

## Project Icon
The following project icon was created with paint.net. Using a screenshot of Powershell executing the creation of 20 Version 1 UUIDs.

![](icon/256.png)

## Note / Limitations
* Limit of the 4 predefined UUID v3/v5 namespaces (URL, DNS, OID, X.500)

## Future Ideas
* ~~Adding support for uuid namespaces, including UUIDv3 and UUIDv5~~
* ~~Graphical User Interface~~
  * Dark Mode
  * Settings Panel (instead of seperate pop-ups)
* Decoding UUIDs

## Shoutouts
Thanks to these github users I was able to figure out how to use tkinter for the GUI.
* [jatinkarthik-tripathy](https://github.com/jatinkarthik-tripathy/Text-Editor)
* [six519](https://github.com/six519/Python-Notepad)
* [code-mentor.org](https://code-mentor.org/notepad-using-tkinter-in-python-with-source-code)

## Run in docker
App can be ran in docker.

### Build image

`docker build . -t uuid`

### Run

```
# UUIDv4
docker run --rm -it uuid:latest

# 5 x UUIDv4
docker run --rm -it uuid:latest -c 5

# Display Help
docker run --rm -it uuid:latest --help
```

