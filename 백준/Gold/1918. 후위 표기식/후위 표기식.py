import sys
input = sys.stdin.readline

def postfix(exp):
    res = []
    ops = []
    order = {'(':0, ')':0, '+': 1, '-': 1, '*': 2, '/':2}

    for item in exp:
        if item in order:
            if item == "(":
                ops.append(item)
            elif item == ")":
                while ops and ops[-1] != "(":
                    res.append(ops.pop())
                ops.pop()
            else:
                while ops and order[ops[-1]] >= order[item]:
                    res.append(ops.pop())
                ops.append(item)
        elif item.isalpha():
            res.append(item)

    while ops:
        res.append(ops.pop())

    return "".join(res)

print(postfix(input()))

