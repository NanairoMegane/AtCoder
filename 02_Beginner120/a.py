# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())
retVal = 0

if a > b:
    retVal = 0
elif b // a < c :
    retVal = b // a
else :
    retVal = c

print(retVal)