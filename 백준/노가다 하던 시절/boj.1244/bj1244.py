n = int(input())    # 1<= 스위치 개수 <= 100
switches = list(map(int, input().split()))    # 스위치 현황
m = int(input())    # 1<= 학생 수 <= 100
students = [[] for _ in range(m)]
for i in range(m):
    students[i] = list(map(int, input().split()))
    #성별, 번호

for student in students:
    if student[0] == 1:     #만약 남자다?
        num = student[1]
        for mul in range(num-1, n, num):
            if switches[mul] == 0:
                switches[mul] = 1
            else:
                switches[mul] = 0
    else:
        idx = student[1]-1
        for j in range(n//2):
            if 0 <= idx-j and idx+j < n and switches[idx+j] == switches[idx-j]:
                if switches[idx+j] == 0:
                    switches[idx+j] = switches[idx-j] = 1
                else:
                    switches[idx+j] = switches[idx-j] = 0
            else:
                break

for k in range(n):
    print(switches[k], end=' ')
    if (k+1) % 20 == 0:
        print()