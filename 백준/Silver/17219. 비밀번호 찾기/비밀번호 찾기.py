import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 저장된 사이트 주소 1 <= N <= 100,000
# 비밀번호 찾으려는 사이트 주소 1 <= M <= 100,000
find = {}
for _ in range(N):
    site, pw = input().split()
    find[site] = pw
#  사이트, 비밀 번호
#  최대 길이 20자

for i in range(M):
    tar = input().split()[0]
    # input 리스트로 저장됨
    print(find[tar])