num1 = input()
num2 = input()
num3 = input()

if num1.isdigit():
    res = int(num1)+3
elif num2.isdigit():
    res = int(num2)+2
else:
    res = int(num3)+1

if res % 15 == 0:
    print('FizzBuzz')
elif res % 3 == 0:
    print('Fizz')
elif res % 5 == 0:
    print('Buzz')
else:
    print(res)