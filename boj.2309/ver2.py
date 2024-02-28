dwarfs = list(int(input()) for _ in range(9))
heightsum = sum(dwarfs)
strangersum = heightsum - 100
flag = 1

while flag:
    for i in range(8):
        for j in range(i+1, 9):
            if dwarfs[i]+dwarfs[j] == strangersum:
                dwarfs.pop(i)
                dwarfs.pop(j-1)
                dwarfs.sort()
                flag = 0
                break
        if not flag:            #이거 8행으로 올려도 맞는이유뭐임...뭐임...뭐임..->인덱스로 안 써서...오류 안 남,,,
            break
print(*dwarfs, sep='\n')
