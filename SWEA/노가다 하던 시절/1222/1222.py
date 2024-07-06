# import sys
# sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    tks = input()
    stack = []
    answer = ''

    for tk in tks:
        if tk == '+':   # 연산자일 경우
            while stack:    # 순위 낮은 연산자 나올 때까지(빌 때까지)
                answer += stack.pop()   #pop
            stack.append(tk) #다 뺐으면 push 해주세요
        else:
            answer += tk

    while stack:
        answer += stack.pop()


    for tk in answer:
        if tk != '+':
            stack.append(int(tk))   # 빈 스택 재활용하겠습니다.
        else:
            num_1 = stack.pop()
            num_2 = stack.pop()
            final_num = num_1 + num_2
            stack.append(final_num)

    print(f'#{tc} {final_num}')