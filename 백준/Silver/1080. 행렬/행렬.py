import sys
input = sys.stdin.readline

def switch(r, c, arr):
    global cnt
    cnt += 1

    for i in range(3):
        arr[r+i][c:c+3] = [1 - x for x in arr[r+i][c:c+3]]

    return

n, m = map(int, input().split())
a = list(list(map(int, input().strip())) for _ in range(n))
b = list(list(map(int, input().strip())) for _ in range(n))

if a == b:
    cnt = 0

elif n < 3 or m < 3:
    cnt = -1

else:
    cnt = 0

    for row in range(n-2):
        for col in range(m-2):
            if a[row][col] != b[row][col]:
                switch(row, col, a)
        if a[row] != b[row]:
            cnt = -1
            break

    # 마지막 두 줄에 대한 검사 필요
    if a[-2:] != b[-2:]:
        cnt = -1
print(cnt)