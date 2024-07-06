import sys
sys.stdin = open('input.txt')
from collections import deque

def whoisthelast(s):
    q = deque()     #  큐 생성
    person = s  # 시작점 설정
    q.append(person)    # 시작점 인큐
    visited[person] = 1 # 시작점 방문 표시

    while q:    # 큐가 빌 때까지
        person = q.popleft()            # 디큐
        for friend in contact[person]:
            if visited[friend] == 0:    # 전화 못 받은 친구가 있다면
                q.append(friend)
                visited[friend] = visited[person] + 1 # 몇 번째로 받았는가

    maxorder = 0
    lastperson = 0
    for i in range(len(visited)):
        if maxorder < visited[i]:
            maxorder = visited[i]
            lastperson = i
        elif maxorder == visited[i]:
            if lastperson < i:
                lastperson = i

    return lastperson






T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    ipt = list(map(int, input().split()))
    contact = list([0]*101 for _ in range(101))
    visited = [0]*101
    for i in range(N//2):
        calling = ipt[2*i]
        receiving = ipt[2*i+1]
        if receiving not in contact[calling]:   # 중복 방지
            contact[calling].append(receiving)

    print(f'#{tc} {whoisthelast(start)}')