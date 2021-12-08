print('Сумма факториалов')

# Программа запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

number = int(input('Введите число: '))

summa = 0

for i in range(1, number + 1):
  factorial = 1
  for j in range(1, i + 1):
    factorial *= j
  summa += factorial

print('Сумма факториалов от 1 до', number, 'равна', summa)
