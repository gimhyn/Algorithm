import math

start = (1, 1)
end = (2, 2)
start2 = (3, 5)
end2 = (1, 4)

a = abs(end[0] - start[0])
b = abs(end[1] - start[1])
a2 = abs(end2[0] - start2[0])
b2 = abs(end2[1] - start2[1])

r = math.sqrt(a**2 + b**2)
r2 = math.sqrt(a2**2 +b2**2)

print(r)
# print(r2)
radian = math.atan(b/a)
print(r, math.degrees(radian))