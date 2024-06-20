import sys
input = sys.stdin.readline

N, M = map(int, input().split())
never_listened = list(input().strip('\n') for _ in range(N))
never_seen = list(input().strip('\n') for __ in range(M))
# 이름 <= 20, 띄어쓰기 없음, .각 리스트 중복 없음
# N, M <= 500,000

듣보잡 = set(never_listened) & set(never_seen)
print(len(듣보잡))
nugu = sorted(듣보잡, key=lambda x:x)
for p in nugu:
    print(p)
