N = int(input())

i = 0
num = N - 2

while num >= 0:
    num = num - 6*i
    i += 1
if N == 1:
    i = 1
print(i)