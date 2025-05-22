import sys
input = sys.stdin.readline

text = input().strip()
bomb = input().strip()
stack = []

for char in text:
    stack.append(char)
    if len(stack) >= len(bomb) and "".join(stack[-len(bomb):]) == bomb:
        # stack = stack[:-len(bomb)]
        del stack[-len(bomb):]

print("".join(stack) if stack else "FRULA")