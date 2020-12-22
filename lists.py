# if __name__ == '__main__':
#     n = int(input())
#     dataList = []
#
# for x in range(n):
#     commandList = input().split(" ")
#     command = commandList[0]
#     if  (command == 'insert'):
#         index = int(commandList[1])
#         value = int(commandList[2])
#         try:
#             dataList.insert(index, value)
#         except ValueError:
#             continue
#
#     if (command == 'print'):
#             print(dataList)
#
#     if (command == 'remove'):
#         value = int(commandList[1])
#         try:
#             dataList.remove(value)
#         except ValueError:
#             continue
#
#     if (command == 'append'):
#         value = int(commandList[1])
#         try:
#             dataList.apppend(value)
#         except ValueError:
#             continue
#
#     if (command == 'sort'):
#         value = commandList[0]
#         try:
#             dataList.sort()
#         except ValueError:
#             continue
#
#
#     if (command == 'pop'):
#         value = commandList[-1]
#         try:
#             dataList.pop()
#         except ValueError:
#             continue
#
#     if (command == 'reverse'):
#         value = commandList[0]
#         try:
#             dataList.reverse()
#         except ValueError:
#             continue

from itertools import product
color = ["Red", "Blue", "Green"]
brand = ["Lamborghini", "Ferrari", "Bugatti"]
finalCar = list(product(color, brand))
# print(finalCar)

d1 = ('chicken', 'Biriyani')
print([f'{car[0]} - {car[1]}'for car in finalCar])



l = ["e"]
"-".join(str(i) for i in l)


