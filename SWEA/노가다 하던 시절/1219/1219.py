import sys
sys.stdin = open('input.txt')

def findroute(arr):
    start = 0
    end = 99
    stack = []
    visited = [0]*100
    visited[start] = 1
    v = start
    while True:
        for w in arr[v]:
            if w == end:
                return 1
            elif visited[w] == 0:
                stack.append(v)
                visited[w] = 1
                v = w
                break   # 여기 온 애는 else 안 빠지게 break 꼭 걸어주기.
        else:
            if not stack:
                return 0
            else:
                v = stack.pop()


for testcase in range(10):
    tc, N = map(int, input().split())
    # n = 길의 개수
    edge_list = list(map(int, input().split()))
    adj_arr = [[] for i in range(100)]

    for i in range(N):
        start = edge_list[2*i]
        end = edge_list[2*i+1]
        adj_arr[start].append(end)

    print(f'#{tc} {findroute(adj_arr)}')

