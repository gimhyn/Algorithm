import sys
input = sys.stdin.readline

def alpha_to_decimal(a):
    if a == ".":
        return 0
    else:
        return ord(a) - 64

def preorder(idx):
    print(chr(idx+64), end="")
    if left[idx]:
        preorder(left[idx])
    if right[idx]:
        preorder(right[idx])
    return

def inorder(idx):
    if left[idx]:
        inorder(left[idx])
    print(chr(idx + 64), end="")
    if right[idx]:
        inorder(right[idx])
    return

def postorder(idx):
    if left[idx]:
        postorder(left[idx])
    if right[idx]:
        postorder(right[idx])
    print(chr(idx + 64), end="")
    return


N = int(input())
left = [0] * 27
right = [0] * 27

for i in range(N):
    par, lc, rc = map(alpha_to_decimal, input().strip().split())
    left[par] = lc
    right[par] = rc


preorder(1)
print()
inorder(1)
print()
postorder(1)
print()