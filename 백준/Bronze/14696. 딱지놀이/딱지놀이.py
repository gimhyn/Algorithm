n = int(input()) # 1 <= n <= 1000
for round in range(n):
    a_lst = list(map(int, input().split()))
    a = a_lst.pop(0)
    b_lst = list(map(int, input().split()))
    b = b_lst.pop(0)

    a_lst.sort(reverse=True)
    b_lst.sort(reverse=True)
    winner = 'D'
    for i in range(min(a, b)):
        if a_lst[i] > b_lst[i]:
            winner = 'A'
            break
        elif a_lst[i] < b_lst[i]:
            winner = 'B'
            break


    # 짧은 쪽 끝까지 다 봤는데 결과 안 나올 경우
    if winner == 'D':
        if a > b:
            winner = 'A'
        elif b < a:
            winner = 'B'
            
    print(winner)