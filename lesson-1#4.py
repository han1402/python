num = int(input('Insert number '))
big = 0
while num > 0:
    if (num % 10) > big:
        big = num % 10
    num = num // 10
print(f'The biggest number: {big}')