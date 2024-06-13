def stack_order(N):
    stack = []
    for i in range(N):
        order = input()
        if 'push' in order:
            push, num = order.split()
            stack.append(int(num))
        elif order == 'pop':
            if stack:
                res.append(stack.pop())
            else:
                res.append(-1)
        elif order == 'size':
            res.append(len(stack))
        elif order == 'empty':
            if stack:
                res.append(0)
            else:
                res.append(1)
        else:
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)

res = []

N = int(input())
stack_order(N)
for result in res:
    print(result)