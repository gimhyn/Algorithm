import sys
input = sys.stdin.readline

def find_max(arr1, arr2):
    if not arr1 or not arr2:
        return

    tar1, tar2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(tar1), arr2.index(tar2)

    if tar1 == tar2:
        res.append(tar1)
        find_max(arr1[idx1+1:], arr2[idx2+1:])

    elif tar1 > tar2:
        arr1.pop(idx1)
        find_max(arr1, arr2)

    else:
        arr2.pop(idx2)
        find_max(arr1, arr2)


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
res = []

find_max(a, b)

print(len(res))
print(*res)
