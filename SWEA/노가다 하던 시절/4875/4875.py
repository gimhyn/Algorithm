import sys
sys.stdin = open('4875_input.txt')

# 스택 이용해 풀기
class Stack:
    def __init__(self, size):
        self.top = -1
        self.stack = [0] * size

    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        return self.top == len(self.stack) - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print('Full')
            return 0
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print('Empty')
            return 0
        else:
            value = self.peek()
            self.stack[self.top] = 0    # 값 지우기.
            self.top -= 1
            return value

def find_start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                return r, c

def find_path(r, c):
    stack = Stack(N*N)
    stack.push((r, c))
    row, col = r, c
    while not stack.is_empty(): # stack이 비어있다 == 더 이상 이동 불가 & 도착하지 않았을 때(result == 1이면 도착했으니까 더 탐색 ㄴㄴ)
        # 델타 탐핵
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            # 이동할 좌표가 미로 범위 내이고 벽이 아닌 경우
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
                if maze[nr][nc] == '3':
                    return 1
                elif maze[nr][nc] == '0':
                    # 이동할 위치를 방문 처리(벽으로 바꾸기)
                    maze[nr][nc] = '1'  # 다시 탐색할 수 없도록 '1'로 변경(visited대신 사용)
                    # stack에 되돌아올 좌표 저장
                    stack.push((r,c))
                    # 이동
                    row, col = nr, nc
                    break   #  이동한 곳에서 새롭게 델타 탐색해야하니까 멈추기
        else:
        # 더 이상 갈 곳이 없다면 stack에서 pop해서 탐색을 이어나가기
            if not stack.is_empty():
                row, col = stack.pop()

    return 0 # 도착할 수 없음. stack 비었는데 도착 못 한 경우.




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]

    # 델타 탐색을 위한 상,하,좌,우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작 위치를 찾아야 됨
    r, c = find_start()
    # 시작 위치부터 델타 탐색



