# 1 <= 가로, 세로 <= 100
width, height = map(int, input().split())
turn = int(input())
width_list = [0]
height_list = [0]
num  = 1
for i in range(turn):
    dir, cut = map(int, input().split())
    if dir:     # 1은 세로 ->세로로 자르려면 가로 값을 잘라야
        width_list.append(cut)
    else:
        height_list.append(cut)

width_list.append(width)
height_list.append(height)

width_list.sort()   # 앞부터 순서대로 자르지 않을 수도 있으니 정렬
height_list.sort()


max_width = max_height = 0

for j in range(1, len(width_list)): # 바로 바로 값 바꾸면 뒤에 값 제대로 계산 안 될 수도 있음.
    w = width_list[j] - width_list[j-1]
    if max_width < w:
        max_width = w
for k in range(1, len(height_list)):
    h = height_list[k] - height_list[k-1]
    if max_height < h:
        max_height = h

print(max_width*max_height)