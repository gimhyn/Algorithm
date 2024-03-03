width, height = map(int, input().split())
n = int(input())
stores = []

for i in range(n):
    direction, count = map(int, input().split())
    stores.append((direction, count))

dir, cnt = map(int, input().split())    #동근이 현재 위치
s = 0

for store in stores:
    if store[0] == dir:                     # 상점과 동근이가 같은 변에 있다면
        s += abs(cnt - store[1])
    elif dir <= 2:                          # 만약 동근이가 북이나 남쪽에 있다면
        if store[0] <= 2:                   # 상점이 맞은 편에 있다면
            route = cnt + store[1]
            s += height + min(route, 2*width - route)
        else:                               # 상점이 동쪽이나 서쪽에 있다면
            if dir == 1:
                s += store[1]
            else:
                s += height - store[1]

            if store[0] == 3:
                s += cnt
            else:
                s += width - cnt


    elif dir > 2:                           # 만약 동근이가 서쪽이나 동쪽에 있다면
        if store[0] > 2:                    # 만약 상점이 반대편에 있다면
            route = cnt + store[1]
            s += width + min(route, 2*height - route)
        else:                               # 만약 상점이 남쪽이나 북쪽에 있다면
            if dir == 3:                    # 만약 동근이가  서쪽이라면
                s += store[1]
            else:                           # 만약 동근이가 동쪽이라면
                s += width - store[1]

            if store[0] == 1:
                s += cnt
            else:
                s += height - cnt

print(s)