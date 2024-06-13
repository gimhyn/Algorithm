N, M = list(map(int, input().split()))
line1 = 'BWBWBWBW'
line2 = 'WBWBWBWB'
board1 = []
board2 = []

for line in range(4):
    board1.append(line1)
    board1.append(line2)
    board2.append(line2)
    board2.append(line1)

iptlst = list(input() for _ in range(N))

candidates = []
for c in range(M-7):
    for r in range(N-7):
        for i in range(8):
            candidates.append(iptlst[r+i][c:c+8])

res = float('inf')
for i in range(0, len(candidates), 8):
    cnt_1 = 0
    cnt_2 = 0
    for j in range(8):
        for k in range(8):
            if candidates[i+j][k] != board1[j][k]:
                cnt_1 += 1
            if candidates[i+j][k] != board2[j][k]:
                cnt_2 += 1
    if res > min(cnt_1, cnt_2):
        res = min(cnt_1, cnt_2)

print(res)