import sys
input = sys.stdin.readline

a, b, c= map(int, input().split())

def modulo(A, B, C):
    namoji = A % C
    if B == 0:
        return 1

    half = modulo(A, B//2, C)
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * namoji) % C

print(modulo(a, b, c))