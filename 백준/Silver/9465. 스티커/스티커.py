import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    # 1 <= n <= 100,000
    stickers = list(list(map(int, input().strip().split())) for _ in range(2))
		# 스티커 리스트를 만들어줍니다
		
    dp= [[0] * n for _ in range(2)]
    # 똑같은 모양의 dp를 만들고, 
    #윗줄 아랫줄 나눠서 왼쪽(작은 인덱스)부터 차례대로 스캔하며 해당 스티커까지 왔을 때 최댓값을 기록해 볼게요
    
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
		# n = 1이라면 dp는 당연히 해당 스티커 값
		
    if n > 1:
        dp[0][1] = max(stickers[0][1] + stickers[1][0], stickers[0][0])
        dp[1][1] = max(stickers[1][1] + stickers[0][0], stickers[1][0])
        # 만약 n == 2이면 최댓값은 <대각선 방향 index 하나 전과 현재값을 더한 것>과
        # <현재값 포기하고 하나 전 같은 라인만 선택한 것> 중 최댓값이 됩니다.

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1] + stickers[0][i], dp[0][i-1])
            dp[1][i] = max(dp[0][i-1] + stickers[1][i], dp[1][i-1])
						# n이 3이상이면 거기에 같은 라인에서 하나 전 인덱스를 포기하고 현재 값을 선택한 것까지 후보가 추가됩니다.

    print(max(dp[0][n-1], dp[1][n-1]))
    # 두 줄 중 최댓값 고를게요