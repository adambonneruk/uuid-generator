"""scaffolding to test short.py"""
import uuid
from short import shorten_uuid

yep = test_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
print(shorten_uuid(yep))
