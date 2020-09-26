import argparse

def generate(args):
    print("generating...")
    print(args.version)
    print(args.quantity)
    print(args.namespace)
    print(args.name)
    print(args.urn_flag)
    print(args.upper_flag)
    print(args.short_flag)

def decode(args):
    print("decoding...")
    print(args.verbose)
    print(args.a_new_uuid)


def main():

    parser = argparse.ArgumentParser(description="Generate and Decode Version Specific UUIDs",epilog="And that's how you'd foo a bar",allow_abbrev=False)
    subparsers = parser.add_subparsers(help='sub-command help')


    # create the parser for the "b" command
    decoder = subparsers.add_parser('decode')
    decoder.add_argument('a_new_uuid', metavar='UUID', type=str, help='an integer for the accumulator')
    decoder.add_argument('-v', "--verbose",dest="verbose",action="store_true",default=False,help="Provide detailed information about decoded UUID")
    decoder.set_defaults(func=decode_uuid)

    parser.add_argument("-v", "--version",type=int,default=4,dest="version",metavar="<VERSION>",help="Specify output UUID version (0, 1, 3, 4, or 5)")
    parser.add_argument("-q", "--quantity",type=int,default=1,dest="quantity",metavar="<QUANTITY>",help="Specify output quanitity (1 - 65536)")
    parser.add_argument("--ns", "--namespace",type=lambda s: s.lower(),default="",dest="namespace",metavar="<NAMESPACE>",help="UUID v3 or v5 namespace")
    parser.add_argument("-n", "--name",type=str,default="",dest="name",metavar="<NAME>",help="Specify UUID v3 or v4 name")
    #Mutually Exclusive Group
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--urn",dest="urn_flag",action="store_true",default=False,help="Specify URN standard prefix")
    group.add_argument("-U", "--uppercase",dest="upper_flag",action="store_true",default=False,help="Non-standard uppercase UUID string")
    group.add_argument("-s", "--short",dest="short_flag",action="store_true",default=False,help="Shortened UUID using Base64 encoding")
    parser.set_defaults(func=generate_uuid)

    args = parser.parse_args()
    args.func(args)

    print(args)



if __name__ == "__main__":
    main()