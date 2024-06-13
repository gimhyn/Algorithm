from collections import deque
q = deque()
res = []

def orders(n):
    for i in range(n):
        order = input()
        if 'push' in order:
            push, num = order.split()
            q.append(int(num))
        elif order == 'pop':
            if q:
                res.append(q.popleft())
            else:
                res.append(-1)
        elif order == 'size':
            res.append(len(q))
        elif order == 'empty':
            if q:
                res.append(0)
            else:
                res.append(1)
        elif order == 'front':
            if q:
                res.append(q[0])
            else:
                res.append(-1)
        else:
            if q:
                res.append(q[-1])
            else:
                res.append(-1)


N = int(input())
orders(N)
for r in res:
    print(r)