import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
res = set()

def permutations(arr, m, current=[]):
    # m개를 골랐으면 결과를 출력
    if len(current) == m:
        res.add(tuple(current))
        return

    # arr에서 하나씩 선택하면서 순열을 만들기
    for i in range(len(arr)):
        # 현재 선택된 원소를 current에 추가
        next_current = current + [arr[i]]
        # 선택된 원소를 제외하고 나머지 원소로 재귀 호출
        next_arr = arr[:i] + arr[i+1:]
        permutations(next_arr, m, next_current)


permutations(nums, M, [])
res = sorted(list(res))
for ans in res:
    print(*ans)