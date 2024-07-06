import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    len_tc = int(input())
    tks = input()
    p = {'+': 1, '*': 2}
    stack = []
    top = -1
    postfix = ''

    for tk in tks:          # postfix 만들기
        if tk not in '*+':  # 숫자일 때
            postfix += tk
        else:
            if len(postfix) == len_tc: # 다 돌았다면 멈추기
                break
            while p[tk] <= top:         # 만약 연산자 우선순위가 top과 같거나 작다면
                postfix += stack.pop()    # pop
                if stack:
                    top = p[stack[-1]]      # top 갱신
                else:
                    top = -1    #스택 비었으면 top -1로 갱신
            stack.append(tk)
            top = p[stack[-1]]

    while stack:   # 스택에 남은 연산자 처리
        postfix += stack.pop()

    for char in postfix:
        if char not in '+*':
            stack.append(int(char))
        else:
            if char == '+':
                answer = stack.pop()+stack.pop()
                stack.append(answer)
            else:
                answer = stack.pop()*stack.pop()
                stack.append(answer)

    print(f'#{tc} {stack[-1]}')