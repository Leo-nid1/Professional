


# # books = {'Евгений Онегин': 'А. С. Пушкин', 'Горе от ума': 'А. С. Грибоедов', 'Преступление и наказание': 'Ф. М. Достоевский'}
# # while True:
# #     try:
# #         a = input()
# #         c = books[a]
# #         print(c)
# #     except Exception as e:
# #         print(e)
#
# while True:
#     file = []
#     ind = 0
#     try:
#         f = open(input(), 'r', encoding='UTF-8')
#         for line in f:
#             file.append(line)
#         for i in file:
#             for e in range(len(i)):
#                 ind += 1
#         if ind > 100:
#             raise ValueError()
#         for f in file:
#             print(f.strip())
#         f.close()
#     except Exception:
#         pass
#     except UnicodeDecodeError:
#         print('Невозможно раскодировать')






# name = input('Имя: ')
# if name[0].islower():
#     raise TypeError()
# name = input('Фамилия: ')
# if name[0].islower():
#     raise TypeError()











class PentagonCrash(Exception):
    def __init__(self):
        self.text = ' ВЫ САМИ ЭТО СКАЧАЛИ! '
        file = open("virus.py", "w", encoding='UTF-8')
        file.write('print("Пентагон взломан")')
        file.close()
    def __str__(self):
        return self.text
raise PentagonCrash