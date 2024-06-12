N, K = list(map(int, input().split()))
memoization = {0:0, 1:1}
def factorial(num):
    if num in memoization:
        return memoization[num]
    else:
        memoization[num] = num*factorial(num-1)
        return memoization[num]


if K == N or K == 0:
    print(1)
else:
    print(factorial(N) // (factorial(K) * factorial(N-K)))