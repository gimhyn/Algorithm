import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mod(num, power, deno):
    remainder = num % deno
    if power == 0:
        return 1

    if power % 2: # 홀수면
        half = mod(num, power//2, deno)
        return (half * half * remainder) % deno
    else: # 짝수면
        half = mod(num, power//2, deno)
        return (half * half) % deno

print(mod(A, B, C))