# print('I\'m John, - сказал он и отвернулся')
# s1 = 'Hello,
#      world'
# s2 = "Hello,
#      world"
# s3 = '''Hello,
#      world''' #  тройных кавычках можно разрывать строку
# print('Hello', 'world', '!', sep='*')
# print('Hello', 'world', '!', end='')
# print('Hello', 'world', '!', end='')

# # Примтивные типы
# tom_age = 5  # int
# weight = 50.5  # float
# is_published = True  # bool
# n = None  # NoneType - ничего

# # Составные
# name = 'Alex'  # str строка
# my_list = [1, 2, 3]  # списки
# my_set = {1, 2, 3, 4, 5}  # множества
# my_dict = {2: 'two'}  # словари
#
# a = 9
# b = 2
# print(a + b, a - b, a / b, a * b)
# print(a // b, a % b)
# print(a ** b, a ** (1 / b))


# a = int(input())
# b = int(input())
# print(a + b)

# c = 7
# print(type(c))
# c = str(c)
# print(type(c))
# Задача 1
# print(input())
#
# # Задача 2
# number = int(input())
# print(number % 10)


# Задача 3
# gift = int(input())
# price = int(input())
# print(12000 + gift - price)


# a = 7
# line = 'Python is the best language'
# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])
# print(b[4])
# print(b[5])
# Срезы
# print(line[0:3])  # от нулевого до 3 НЕ включительно
# print(line[2:])  # от второго до конца
# print(line[:5])  # от нулевого до 5 НЕ включительно
# print(line[1:9:2])  # от первого до 9 НЕ включительно через 1
# print(line[::-1])  # от первого до 9 НЕ включительно через 1
#
# line2 = input()
# print(line2[len(line2) - 1])  # len() возвращает длину строки
# print(line2[-1])  # выводим последний символ


# line3 = 'Hello'
# print(line3)
# line3 = 'Bye'
# print(line3)
# for i in range(1, 2000):
#     print(i, '=>', chr(i))

#
# print('hello' == 'Hello')
# print('hello' == 'hello')
# print('hеllo' == 'hello')
# print('hеllo' + 'hello')

# Форматированные строки
a = int(input())
b = int(input())
print(f'Сумма чисел {a} и {b} = {a + b}')


a = int(input())
b = []
count = 0
h = 0
for i in range(a):
    b.append(int(input()))
c = int(input())
d = int(input())
for i in range(c - 1, d):
    count += b[i]

print(count // 60, 'ч.', count % 60, 'минут.')

s = int(input())
y = s * s + s + 10
print(y)

a = int(input())
s = []
for i in range(a * 2):
  s.append(int(input()))
print(s)