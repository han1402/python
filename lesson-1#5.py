rev = int(input('Введите выручку фирмы '))
costs = int(input('Введите издержки фирмы '))
if rev > costs:
    print(f'Фирма приносит прибыль с разницей {rev / costs}')
    num = int(input('Введите количество сотрудников '))
    print(f'Прибыль на одного сотрудника составляет {(rev - costs) / num}')
elif rev < costs:
    print('Фирма приносит убытки')
else:
    print('Фирма выходит в ноль по прибили')