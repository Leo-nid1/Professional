



a = ['20', '30', 'Маргарита', True]
b = a.copy()  # возвращает независимую копию списка а
b2 = list(a)
a[1] = 'hello'
print(b)
print(id(a))

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[2][1])

if 'Маргарита' not in a:
    print('Ее нет в списке приглашенных')
else:
    print('Она в списке приглашенных')

#Генераторы списков
lst = [10, 24, 56, 78]
lst2 = lst * 5
print(lst2)
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

numbers2 = [i for i in range(1, 11)]
print(numbers2)

numbers3 = [i // 2 for i in range(1, 11)]
print(numbers3)

numbers4 = [i * 3 for i in numbers3]
print(numbers4)

numbers1 = [1, 2, 3, 4, 5, 6, 7]
numbers5 = [i for i in numbers1 if i % 2 == 0 if i % 3 == 0]
print(numbers5)


n = int(input())
m = int(input())
week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

for i in range(n):
    print(week[(m - 1 + i) % 7])


a = int(input())
b = []
for i in range(a):
  b.append(input())

c = []
for i in range(a - 1, -1, -1):
  c.append(b[i])

print('[', end='')
n = b + c
for i in range(len(n) - 1):
  print(n[i], end=', ')
print(n[len(n) - 1], ']', end='', sep='')


######################
a = int(input())
b = []
c = {}
for i in range(a):
  e, e1 = input().split()
  b.append(e)
  b.append(e1)
  c[e] = e1


print(c)



a1 = input()
b1 = input()
a = []
b = []
for i in range(len(a1)):
  a.append(a1[i:i+1])
for i in range(len(b1)):
  b.append(b1[i:i+1])

s = set(a) - set(b)

print(len(a) * 0.3 >= len(s))
