N = int(input())
spots = []
for _ in range(N):
    spots.append(list(map(int, input().split())))

spots.sort(key=lambda x: (x[0], x[1]))
for spot in spots:
    print(spot[0], end=' ')
    print(spot[1])