import uuid

class Celsius:
    def __init__(self, temperature=1):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

class UuidWrapper:
    def __init__(self):
        self.version = 4

    def generate(self):
        if self.version == 1:
            return uuid.uuid1()
        return uuid.uuid4()

foo = UuidWrapper()
foo.version = 1
print(foo.version)
print(foo.generate())

bar = UuidWrapper()
print(bar.version)
print(bar.generate())
