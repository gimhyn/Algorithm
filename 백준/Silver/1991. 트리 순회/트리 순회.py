import sys
input = sys.stdin.readline

def alpha_to_decimal(a):
    if a == ".":
        return 0
    else:
        return ord(a) - 64

def preorder(idx):
    print(chr(idx+64), end="")
    if child[idx][0]:
        preorder(child[idx][0])
    if child[idx][1]:
        preorder(child[idx][1])
    return

def inorder(idx):
    if child[idx][0]:
        inorder(child[idx][0])
    print(chr(idx + 64), end="")
    if child[idx][1]:
        inorder(child[idx][1])
    return

def postorder(idx):
    if child[idx][0]:
        postorder(child[idx][0])
    if child[idx][1]:
        postorder(child[idx][1])
    print(chr(idx + 64), end="")
    return


N = int(input())
child = [(0, 0) for _ in range(27)]

for i in range(N):
    par, left, right = map(alpha_to_decimal, input().strip().split())
    child[par] = (left, right)


preorder(1)
print()
inorder(1)
print()
postorder(1)
print()