import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().strip().split())

z = (d * b - e * a)
if z != 0:
    y = (c * d - f * a) // z
    if a != 0:
        x = ( c - b * y) // a
    else:
        x = (f - e * y) // d
else:
     x = c * e - f * b // (e * a - b * d)
     if b != 0:
        y = (c - a * x) // b
     else:
         y = (f - d * x) // e
     
print(x, y)