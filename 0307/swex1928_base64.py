s = 'A'
if ord('A')<=ord(s) and ord(s)<=ord('Z'):
    n = ord(s)-ord('A')
if ord('a')<=ord(s) and ord(s)<=ord('z'):
    n = ord(s)-ord('a')+26
if ord('0')<=ord(s) and ord(s)<=ord('9'):
    n = ord(s)-ord('1')+52
if ord('+'):
    n = 62
if ord('/'):
    n = 63