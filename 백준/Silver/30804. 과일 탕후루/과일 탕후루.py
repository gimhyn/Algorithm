import sys
input = sys.stdin.readline

N = int(input().strip())
thr = list(map(int, input().split()))

# 최대 길이 변수 초기화
maxlen = 1

# 사전을 사용하여 값과 해당 값의 등장 횟수를 기록
freq = {}
left = 0

for right in range(N):
    # 현재 값의 등장 횟수 기록
    if thr[right] in freq:
        freq[thr[right]] += 1
    else:
        freq[thr[right]] = 1

    # 윈도우 크기가 유니크한 값의 개수보다 크다면 왼쪽 포인터를 이동시킴
    while len(freq) > 2:
        freq[thr[left]] -= 1
        if freq[thr[left]] == 0:
            del freq[thr[left]]
        left += 1

    # 최대 길이 업데이트
    maxlen = max(maxlen, right - left + 1)

print(maxlen)