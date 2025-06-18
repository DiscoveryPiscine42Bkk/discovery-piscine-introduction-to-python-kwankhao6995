import sys

def dewncase_it(s):
   return s.lower()

args = sys.argv[1:]

1f not args:
    print("Hello world")
else:
    for arg in args:print(downcase_it(arg))