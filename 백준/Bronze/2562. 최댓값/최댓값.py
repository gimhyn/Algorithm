lst = []
for _ in range(9):
    lst.append(int(input()))

maximum = max(lst)
print(maximum)
print(lst.index(maximum)+1)