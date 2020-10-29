from platform import python_implementation, python_version_tuple

print(python_implementation())

# python_version_tuple() → returns a three-element tuple filled with:
# the major part of Python's version;
# the minor part;
# the patch level number.

for atr in python_version_tuple():
    print(atr)