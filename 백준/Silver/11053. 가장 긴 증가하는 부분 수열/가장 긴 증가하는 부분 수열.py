# 백준 11053번: 가장 긴 증가하는 부분 수열

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # 모든 원소는 최소 길이 1의 LIS를 가질 수 있음
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 입력
n = int(input())
arr = list(map(int, input().split()))

# 결과 출력
print(longest_increasing_subsequence(arr))
