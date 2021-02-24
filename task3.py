#!/usr/bin/env python

s = input().split()
print(' '.join([x[::-1] for x in s]).strip())
