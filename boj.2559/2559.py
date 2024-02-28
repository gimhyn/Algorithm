n, k = map(int, input().split())
lst = list(map(int, input().split()))
#
# sum = 0
#
# for i in range(k):
#     sum += lst[i]
#
# max_sum = sum
# for i in range(1, n-k+1):
#     sum = sum - lst[i-1] + lst[i+k-1]
#     if max_sum < sum:
#         max_sum = sum
#
# print(max_sum)
sum_lst = []

for i in range(n - k + 1):
    sum = 0
    for j in range(k):
        sum += lst[i + j]
    sum_lst.append(sum)

print(max(sum_lst))