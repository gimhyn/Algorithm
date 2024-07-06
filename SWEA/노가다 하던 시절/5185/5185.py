import sys
sys.stdin = open('5185_input.txt')

def hex_to_bin(num):
    d = {'0':'0000',
            '1':'0001',
            '2':'0010',
            '3':'0011',
            '4':'0100',
            '5':'0101',
            '6':'0110',
            '7':'0111',
            '8':'1000',
            '9':'1001',
            'A':'1010',
            'B':'1011',
            'C':'1100',
            'D':'1101',
            'E':'1110',
            'F':'1111'
         }
    res = ''
    for char in num:
        res = res+d[char]
    return res

T = int(input())
for tc in range(1, T + 1):
    n, num = input().split()
    # str주의
    print(f'#{tc} {hex_to_bin(num)}')