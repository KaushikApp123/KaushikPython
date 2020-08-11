# cost = 100
# qty = 50
# spoilt = 10
# totalSales = (qty * cost)-(spoilt * cost)
# print(totalSales)
#
# cost = 169
# qty = 53
# spoilt = 16
# totalSales = (qty * cost)-(spoilt * cost)
# print(totalSales)
#
# def calculateSales(cost, qty, spoilt):
#     totalSales  = (qty * cost)-(spoilt * (cost * 0.8))
#     print(totalSales)
#
# calculateSales(10, 30, 19)
# calculateSales(100, 300, 109)
#
# # 1000.00 8% 2
# # ( p * r )* d + p
#
# def calculateIntrest(principal, rate, duration):
#     total =( (principal * rate) * duration ) + principal
#     print("Principal: %d ; interest = %f ; years = %s; total = %s "%(principal, rate, duration, total))
#     print("Principal: {} ; interest = {} ; years = {}; total = {} ".format(principal, rate, duration, total))
#     print("Principal: {p} ; interest = {i} ; years = {y}; prinicple = {p} ".format(p = principal, i = rate, y = duration))
#     print("Principal: {0} ; interest = {1} ; years = {2}; prinicple = {0} ".format(principal,rate,duration))
#     return total
#
# principleAmount = 1000
# #int(input("what is the principle amount? "))
# print(principleAmount)
# t1 = calculateIntrest(principleAmount, 0.08, 2)
# t2 = calculateIntrest(1090.00, 0.98, 28)
# print("This is T1", t1 )
# print("This is T2", t2 )
# print(int(1.08))


languages = "python"
NumberOfStudents = 3
print("The {} class has {} students".format(languages, NumberOfStudents))

city = "Round Rock"
time = 5
print("{} is {} minutes away by car".format(city,time))