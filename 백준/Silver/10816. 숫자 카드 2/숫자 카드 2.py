import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
count = {}
for card in cards:
    if card not in count:
        count[card] = 1
    else:
        count[card] += 1

M = int(input())
numbers = list(map(int, input().split()))
for number in numbers:
    if number in count:
        print(count[number], end=' ')
    else:
        print(0, end=' ')