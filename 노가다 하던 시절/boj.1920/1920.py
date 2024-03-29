N = int(input())    # N 개의 정수
num_set = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    if i in num_set:
        print(1)
    else:
        print(0)