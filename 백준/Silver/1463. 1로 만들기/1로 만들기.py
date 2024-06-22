def findmin(num):
    for i in range(2, num+1):
        count[i] = count[i - 1] + 1

        if i % 3 == 0:
            count[i] = min(count[i], count[i//3] + 1)

        if i % 2 == 0:
            count[i] = min(count[i], count[i//2] + 1)

    return count[num]


import sys
input = sys.stdin.readline
count = [0]*(10**6 + 1)

N = int(input())
print(findmin(N))
