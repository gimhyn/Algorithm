import sys
input = sys.stdin.readline

S = set()
full = {i for i in range(1, 21)}
M = int(input())

for action in range(M):
    ipt = input().strip()
    if 'all' in ipt:
        act = 'all'
    elif 'emp' in ipt:
        act = 'empty'
    else:
        act, num = ipt.split()
        num = int(num)

    if act == 'add':
        S.add(num)
    elif act == 'remove':
        S.discard(num)
        # 없는 숫자 없애려할 때도 있다는 걸..
    elif act == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif act == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif act == 'all':
        S.update(full)
    else:
        S.clear()
