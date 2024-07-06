# import sys
# sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    length = int(input()) #찾아야 하는 회문의 길이. 가로/세로만
    puzzle = list(list(input()) for _ in range(8))
    count = 0

    # 가로 찾기
    for r in range(8):
        for c in range(8-length+1):
            if puzzle[r][c:c+length] == puzzle[r][c:c+length][::-1]:
                count += 1

    # 행렬 바꾸기
    puzzle = list(map(list, zip(*puzzle)))

    # 세로 찾기
    for r in range(8):
        for c in range(8-length+1):
            if puzzle[r][c:c+length] == puzzle[r][c:c+length][::-1]:
                count += 1

    print(f'#{tc} {count}')