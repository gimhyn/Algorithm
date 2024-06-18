def roundUp(num):
    if num % 1 * 2 >= 1:
        num = num // 1 + 1
    else:
        num //= 1

    return int(num)

import sys
input = sys.stdin.readline

N = int(input())
numbers = []
cnt = {}
for _ in range(N):
    number = int(input())
    if number not in cnt:
        cnt[number] = 1
    else:
        cnt[number] += 1
    numbers.append(number)

print(roundUp(sum(numbers)/N))
numbers.sort()
print(numbers[(N+1)//2 - 1])

most_common = max(cnt.values())
res = []
for k, v in cnt.items():
    if v == most_common:
        res.append(k)
res.sort()
if len(res) == 1:
    print(res[0])
else:
    print(res[1])
print(max(numbers) - min(numbers))