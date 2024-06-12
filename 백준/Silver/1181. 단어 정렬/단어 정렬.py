N = int(input())
# 1 <= N <= 20000

words = set()

for _ in range(N):
    word = input()
    if word not in words:
        words.add(word)

newdict = sorted(words, key=lambda x:(len(x), x))

for nw in newdict:
    print(nw)