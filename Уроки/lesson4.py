a = {1, 2, 2, 2, 4, 3, 5}
a1 = {1, 2, 2, 2, 4, 3, 5, 6, 7, 8, 9, 3, 4, 5, 6}
b = {'red'}
v = {45, 'uyu', '0'}
c = a.union(b)
print(v | a)
print(a1 - a)
print(len(a - b | v))
print(len(a - b) >= 3)

dict1 = {'ant' : 'bee', 1 : 'one'}
dict1['ant'] = 'bees'
print(dict1['ant'])

a, b = input().split()


while a != '6' and b != '6':
  a, b = input().split()