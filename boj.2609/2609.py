a, b = map(int, input().split())

def divisor(N):
    divisor_set = set()
    for i in range(1, int(N**(1/2))+1):
        if N % i == 0:
            divisor_set.add(i)
            divisor_set.add(N//i)
    return divisor_set

common_divisor = sorted(list(divisor(a) & divisor(b)))
multiple = sorted(list(divisor(a)|divisor(b)))
lcm = a*b
for num in multiple[::-1]:
    if (lcm/num) % a == 0 and (lcm/num) % b == 0:
        lcm //= num

print(common_divisor[-1])
print(lcm)