N = int(input())
dic = {}

for i in range(N):
    r, c, w, h = map(int, input().split())
    for x in range(r, r+w):
        for y in range(c,c+h):
            dic[(x,y)] = i
lst = list(dic.values())
for j in range(N):
    print(lst.count(j))
