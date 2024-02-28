M, N = map(int,input().split()) # 1<= M <= N<=1,000,000

num = [0]*M + [1]*(N - M + 1)
prime = []
for i in range(2, len(num)):
    if num[i]:
        prime.append(i)
    for j in range(2*i, N+1, i):
        if num[j]:
            num[j] = 0

for prime_number in prime:
    print(prime_number)