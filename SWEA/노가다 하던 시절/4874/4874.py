# import sys
# sys.stdin = open('4874_input.txt')

T = int(input())
for tc in range(1, T+1):
    infix = input().split()         # 256자 이내
    stack = []
    num_cnt = 0
    op_cnt = 0

    for tk in infix:
        if tk not in '*/+-.':       # 숫자는
            num_cnt += 1
            stack.append(int(tk))   # 스택에 넣기
        elif tk == '.':             # .은
            if len(stack) < 1:      # 스택에 뽑을 값 없으면
                answer = 'error'    # error
                break
            elif num_cnt != op_cnt+1:   #숫자 개수 != 연산자 개수+1 일 때
                answer = 'error'
                break
            answer = stack[-1]      # 아니면 마지막 값 뽑기
            break

        else:                       # 연산자는
            op_cnt += 1
            if len(stack) < 2:      # 계산 못하는 상황이면
                answer = 'error'    # error
                break
            num2 = stack.pop()      # 아니면 스택에서 값 뽑아 연산
            num1 = stack.pop()
            if tk == '*':
                result = num1*num2
            elif tk == '/':
                result = num1//num2 # 나누어 떨어져도 소수 변환될 수 있으니 //
            elif tk == '+':
                result = num1+num2
            else:
                result = num1-num2
            stack.append(result)    # 결과는 스택에 다시 넣어주삼요


    print(f'#{tc} {answer}')