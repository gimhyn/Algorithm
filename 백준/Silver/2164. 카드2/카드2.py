from collections import deque
N= int(input())
cards = deque([i for i in range(1, N+1)])
while len(cards) >= 2:
    cards.popleft()
    cards.rotate(-1)
print(*cards)