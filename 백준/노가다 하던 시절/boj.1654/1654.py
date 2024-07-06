K, N = map(int,input().split()) # K개의 랜선 잘라서 N개 만들어야해
# 1 <= K <= 10,000 // K <= N <= 1,000,000

len_list = list(int(input()) for _ in range(K))

start = 0
end = min(len_list)
max = (start + end) // 2

count = 0
while count != N:
    count = 0

    for lan in len_list:
        count += lan // max

    if count < N:
        end = max
        max = (start + end) // 2

    elif count > N:
        start = max
        max = (start + end) // 2

while count == N:
    for lan in len_list:
        count += lan // max
    max += 1

print(max)

