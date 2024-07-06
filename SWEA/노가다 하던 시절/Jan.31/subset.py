N = 3
arr = [1, 2, 3]

for i in range(1<<N):
    s= 0
    for j in range(N):
        if i&(1<<j):
            s += arr[j]
            print(arr[j], end = ' ')
    print(s)