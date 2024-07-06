import sys
sys.stdin = open('input.txt')

def makemax(c):
    global ans
    if c == change:
        res = int(''.join(num_list))
        if ans < res:
            ans = res
        return
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            makemax(c+1)
            num_list[i], num_list[j] = num_list[j], num_list[i]


T = int(input())
for tc in range(1, T+1):
    nums, change = input().split()
    num_list = list(num for num in nums)    # str 주의
    min_v = min(list(int(num) for num in nums))
    ans = 0
    makemax(0)
    print(f'#{tc} {ans}')



