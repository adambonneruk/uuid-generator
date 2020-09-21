"""short seeks to shorten a hexidecimal uuid returning a base 64 encoded string"""
import logging
import uuid
import codecs

def shorten_uuid(input_uuid):
    """convert hexidecimal uuid to base64"""
    logging.debug("shorten_uuid():")

    str_uuid = str(input_uuid)
    logging.debug("str_uuid: %s", str_uuid)

    hex_uuid = uuid.UUID(str_uuid).hex
    logging.debug("hex_uuid: %s", str(hex_uuid))

    bin_uuid = codecs.decode(hex_uuid, "hex")
    logging.debug("bin_uuid: %s", str(bin_uuid))

    b64_uuid = codecs.encode(bin_uuid, "base64")
    logging.debug("b64_uuid: %s", str(b64_uuid))

    output_uuid = str(b64_uuid)[2:-3]
    logging.debug("output_uuid: %s", output_uuid)

    return output_uuid

def elongate_uuid(input_uuid):
    """"convert base64 to hexadecimal uuid"""
    logging.debug("elongate_uuid():")

    b64_uuid = input_uuid.encode("ascii")
    logging.debug("b64_uuid: %s", str(b64_uuid))

    bin_uuid = codecs.decode(b64_uuid, 'base64')
    logging.debug("bin_uuid: %s", str(bin_uuid))

    hex_uuid = codecs.encode(bin_uuid, 'hex')
    logging.debug("hex_uuid: %s", str(hex_uuid))

    str_uuid = uuid.UUID(str(hex_uuid)[2:-1].zfill(32))
    logging.debug("str_uuid: %s", str(str_uuid))

    output_uuid = str(str_uuid)

    return output_uuid

def main():
    """using main for testing purposes"""
    debug = True
    if debug:
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    logging.debug("__main__")

    test_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))
    logging.debug("test uuid: %s", test_uuid)

    encoded_uuid = shorten_uuid(test_uuid)
    logging.debug("base64 encoded uuid: %s", encoded_uuid)

    print("===========================")

    decoded_uuid = elongate_uuid(encoded_uuid)
    logging.debug("...and back again: %s", decoded_uuid)

    little_uuid = elongate_uuid("QACgAAAAAAAL/w==")
    logging.debug("...and back again: %s", little_uuid)

if __name__ == "__main__":
    main()
