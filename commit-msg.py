#!/usr/bin/python

import re
import sys

message = sys.argv[0]
pattern = re.compile('^([A-Z]+) (#[0-9]+) - ([A-Z][a-zA-Z ]+)$')
test = pattern.match(message)

print(message)
if test == None:
	print('Invalid commit message')
	sys.exit(1)
else:
	print('Valid commit message')
	sys.exit(0)
