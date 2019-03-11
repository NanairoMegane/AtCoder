# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())

max = max(a, b) + 1
if max > 101:
    max = 101

list = []

for ta in range(max):
    if ta == 0:
        continue
    elif a % ta == 0 and b % ta == 0:
        list.append(ta)

print(list[-c])