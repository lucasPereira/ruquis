#!/usr/bin/python

import re
import sys

messageFile = sys.argv[1]
message = open(messageFile, 'r').read()
pattern = re.compile('^([A-Z]([ ]?[a-zA-Z]+)*)$', re.M)
test = pattern.search(message)

if test == None:
	print('Invalid commit message')
	sys.exit(1)
else:
	sys.exit(0)
