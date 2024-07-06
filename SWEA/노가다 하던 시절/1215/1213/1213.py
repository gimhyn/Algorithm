# import sys
# sys.stdin = open('test_input.txt', encoding='utf-8')

T = 10

for tc in range(1, T+1):
    testcase = input()
    pattern = list(input())   # 1<= len(pattern) <= 10
    target = list(input())    # target <= 1000
    count = 0

    for i in range(len(target) - len(pattern) + 1):

        for p_idx in range(len(pattern)):
            if pattern[p_idx] == target[i + p_idx]:
                p_idx += 1
            else:
                break
        else:
            count += 1


    print(f'#{tc} {count}')

