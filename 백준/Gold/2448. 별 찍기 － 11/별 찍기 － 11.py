n = int(input())

board = [[' '] * (n*2 - 1) for _ in range(n)]

def triangle(num, x, y): # 밑변, dnl 꼭짓점 x,y좌표
    # 가장 작다면
    if num == 3:
        # 그린다
        board[y][x-1] = '*'
        board[y+1][x-2], board[y+1][x] = '*', '*'
        board[y+2][x-3:x+2] = ['*']*5
    else:
        # 좌측 삼각형 그리기
        triangle(num//2, x - num//2, y + num//2)
        # 우측 삼각형 그리기
        triangle(num//2, x + num//2, y + num//2)
        # 위 삼각형 그리기
        triangle(num//2, x, y)

def draw(num):
    triangle(num, num, 0)
    for line in board:
        print(''.join(line))

draw(n)