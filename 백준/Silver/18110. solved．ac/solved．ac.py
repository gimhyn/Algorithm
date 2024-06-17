def roundUp(num):
    if (num % 1) * 2 >= 1:
        num = num // 1 + 1
    else:
        num = num // 1

    return int(num)

import sys
n = int(sys.stdin.readline())
if n != 0:
    rates = list(int(sys.stdin.readline()) for _ in range(n))
    rates.sort()
    cnt = len(rates)
    end = roundUp(cnt * 0.15)
    # print(end, type(end))
    official_rate = roundUp(sum(rates[end:cnt-end])/(cnt - 2 * end))
    print(official_rate)
else:
    print(0)