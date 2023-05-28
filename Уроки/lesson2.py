
#print("Добро пожаловать в интернет-банк!")
#print("У нас фантастические процентные ставки!")
#print("Для вкладов до 10 тысяч ₽ включительно прибыль составит 10%,")
#print("для вкладов на сумму до 100 тысяч включительно - 20%,")
#print("для более 100 тысяч - 30%!")
#print("На какую сумму желаете сделать вклад?")
#money = int(input())
#if 10000 <= money <100000:
#    money *= 1.1
#if 100000 <= money <1000000:
#    money *= 1.2
#if 1000000 <= money:
#    money *= 1.3

#print("Вы получаете", money, "₽, поздравляем!")

#color = input()
#match color:
 #   case 'debug_stick':
  #      print("OK: 224440")
   # case '777':
    #    print("Chiter!!!")
    #case _:
     #   print("NO")



for i in range(6):
  print("*" * i + '*')



a = int(input())
#Недель: 1
#Дней: 1
#Часов: 1
#Минут: 1
#Секунд: 2
n = 0
d = 0
ch = 0
m = 0
s = 0
for i in range(a):
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m ==  60:
            m = 0
            ch += 1
            if ch == 24:
                ch = 0
                d += 1
                if d == 7:
                    d = 0
                    n += 1



print('Недель:', n)
print('Дней:', d)
print('Часов:', ch)
print('Минут:', m)
print('Секунд:', s)