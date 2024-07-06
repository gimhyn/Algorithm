dwarfs = list(int(input()) for _ in range(9))
bit = [0] * 9


def subsetsum(i, n, t, c):
    sum = 0
    answer = []
    if c == 7:  # 모든 자리를 다 결정했으면
        for j in range(n):  # bit -> dwarfs0
            if bit[j]:
                sum += dwarfs[j]
            if sum > t:
                break
        if sum == t:
            for k in range(n):
                if bit[k]:
                    answer.append(dwarfs[k])
            answer.sort()
            return answer
    elif i == 9:
        return
    else:
        bit[i] = 1
        a = subsetsum(i + 1, n, t, c+1)
        if a:
            return a
        bit[i] = 0
        b = subsetsum(i + 1, n, t, c)
        if b:
            return b

print(*subsetsum(0, 9, 100, 0), sep='\n')