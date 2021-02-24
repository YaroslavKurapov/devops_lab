#!/usr/bin/env python

s = input().lower().strip()
if s == s[::-1]:
    print("yes")
else:
    print("no")
