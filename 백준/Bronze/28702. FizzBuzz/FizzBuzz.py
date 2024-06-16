nums = [input() for _ in range(3)]


new_nums = []
for i in range(3):
    if 'zz' not in nums[i]:
        res = int(nums[i])+(3 - i)
        break
    elif nums[i] == 'Fizz':
        new_nums.append(3)
    elif nums[i] == 'Buzz':
        new_nums.append(5)
    else:
        new_nums.append(15)

while True:
    if res:
        break
    for j in range(10000000-1):
        a = new_nums[0] * j
        b = a + 1
        c = b + 1
        if b % new_nums[1] == 0 and c % new_nums[2] == 0:
            res = c + 1
            break

if res % 15 == 0:
    print('FizzBuzz')
elif res % 3 == 0:
    print('Fizz')
elif res % 5 == 0:
    print('Buzz')
else:
    print(res)