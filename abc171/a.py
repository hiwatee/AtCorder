import re

a = input()

if re.match(r'[A-Z]', a) is not None :
    print("A")

if re.match(r'[a-z]', a) is not None:
    print("a")