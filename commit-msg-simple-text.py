#!/usr/bin/python
# coding: utf-8

import re
import sys

messageFile = sys.argv[1]
message = open(messageFile, 'r').read()
pattern = re.compile('^([A-ZÁ]([ ]?[a-zA-ZãÃáÁàÀõÕóÓéÉíÍúÚçÇ]+)*)$', re.MULTILINE|re.UNICODE|re.LOCALE)
test = pattern.match(message);
if test == None or len(test.groups()) == 0:
	print('Mensagem de commit inválida. A mensagem deve possuir apenas letras e deve começar com letra maiúscula.')
	sys.exit(1)
else:
	sys.exit(0)
