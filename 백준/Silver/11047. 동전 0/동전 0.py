import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 1 <= N(종류) <= 10, 1 <= K <= 100,000,000
coins = [1]
min_coin = int(input())
for _ in range(N-1):
    next_coin = int(input())
    coins.append(next_coin//min_coin)
# 동전은 배수로 늘어남. 최소 1원 최대 1,000,000원
cnt = K // min_coin
res = 0
coins.sort(reverse=True)
for coin in coins:
    res += cnt // coin
    cnt %= coin
    if not cnt:
        break

print(res)