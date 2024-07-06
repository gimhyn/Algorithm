n = int(input())    # n개의 정수
stack = [1]
lst = (int(input()) for _ in range(n))
#43687521

for i in range (2, n+1):
    if stack[-1] < num:
        stack.append(i)
        # print('+')
    elif stack[-1] >