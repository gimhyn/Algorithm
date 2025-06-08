import sys
s= sys.stdin.readline().strip()

alpha = 'abcdefghijklmnopqrstuvwxyz'

for c in alpha:
    print(s.find(c))