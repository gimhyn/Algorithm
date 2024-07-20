import sys
input = sys.stdin.readline

N = int(input().strip())
X = list(map(int, input().strip().split()))
Y = sorted(list(set(X))) # 중복 제거용
my_dict = {Y[i]: i for i in range(len(Y))}
for x in X:
    print(my_dict[x], end=' ')