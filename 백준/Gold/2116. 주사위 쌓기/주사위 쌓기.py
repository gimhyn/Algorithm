num = int(input())
upside = 0
maxsum = 0
first_dice = list(map(int, input().split()))
input_list = list(list(map(int, input().split())) for _ in range(num-1))
def f_dice(us):     # 각각의 윗면에 대한 옆면 최대치 구하기
    a, b, c, d, e, f = first_dice
    afl = [a, f]
    bdl = [b, d]
    cel = [c, e]
    if us in afl:
        s = max(bdl + cel)
    elif us in bdl:
        s = max(afl + cel)
    else:
        s = max(afl + bdl)
    return s

for idx in range(6):
    upside = first_dice[idx]
    sidesum = f_dice(upside)

    for dice in input_list: # 2 ~ n번째 주사위에 대해
        a, b, c, d, e, f = dice
        af = [a, f]
        bd = [b, d]
        ce = [c, e]

        if upside in af:
            sidesum += max(bd+ce)
            if upside == a:
                upside = f
            else:
                upside = a
        elif upside in bd:
            sidesum += max(af+ce)
            if upside == b:
                upside = d
            else:
                upside = b
        else:
            sidesum += max(af+bd)
            if upside == c:
                upside = e
            else:
                upside = c

    if maxsum < sidesum:
        maxsum = sidesum

print(maxsum)