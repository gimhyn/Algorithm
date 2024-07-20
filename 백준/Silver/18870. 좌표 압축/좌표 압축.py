import sys
input = sys.stdin.readline

N = int(input().strip())
X = list(map(int, input().strip().split()))
my_dict = {}
Y = sorted(X)
cnt = 0
num = 0
for i in range(N):
    if i < N-1 and Y[i] == Y[i+1]:
        cnt += 1
    else:
        for j in range(i-cnt, i+1):
            my_dict[Y[j]] = num
        cnt = 0
        num += 1

for x in X:
    print(my_dict[x], end= ' ')
'''
1 <= N <= 1,000,0000
시작은 무조건 0
그다음으로 작은 거 1
sort했을 때 index순
'''