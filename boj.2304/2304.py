N= int(input())
lst = list(map(int, input().split()) for _ in range(N))
# 좌측 좌표, 높이
l_list = [lst[2*i] for i in range(N)]
h_list = [lst[2*i+1] for i in range(N)]
# 최고 높이 갱신 될 때마다 잘라서 사각형 넓이 합 구하기
# square_sum = 0
# 가장 밑 단
def square(arr):
    square_sum = 0
    max_h = max(arr)
    max_h_idx = -1
    max_h_lst = []  # 최대 높이 기둥의 인덱스 받을 리스트
    while l_list[max_h_lst][0] != l_list[0] and l_list[max_h_list][-1] != l_list[-1]:
        width = 0
        while max_h in arr:
            max_h_idx = h_list.index(max_h)
            max_h_lst.append(h_list[max_h_idx])
            arr[max_h_idx] = -1
        square_sum += (abs(l_list[max_h_lst][0] - (l_list[max_h_lst][-1]+1))-width) * max_h
        width = abs(l_list[max_h_lst][0] - (l_list[max_h_lst][-1]+1))

print(square(h_list))