import sys
from itertools import combinations
input = sys.stdin.readline

n, c = map(int, input().split())
# n <= 5000, c<= 10^8
weights = list(map(int, input().split()))
weights.sort()
# w <= 10^8

flag = 0
if c in weights:
    flag = 1
else:
    i = 0
    j = n-1

    while i < j:
        weightsum = weights[i]+weights[j]
        if weightsum > c:
            j -= 1
        elif weightsum == c:
            flag = 1
            break
        else:
            rest = c - weightsum
            if rest in weights and rest not in [weights[i], weights[j]]:
                flag = 1
                break
            i += 1

print(flag)