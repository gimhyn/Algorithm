import sys
import re

T = int(input())
p = re.compile('(100+1+|01)+')

for tc in range(T):
    l = sys.stdin.readline().strip()
    if re.fullmatch(p, l):
        print('YES')
    else:
        print('NO')