import sys
input  = sys.stdin.readline

def inverse(a, mod):
    return pow(a, mod-2, mod)

m = int(input())
res = 0
MOD = 1000000007
for i in range(m):
    n, s = map(int, input().split())
    # q = s / n
    b = inverse(n, MOD)
    res += s * b % MOD
    res %= MOD
    
print(res)