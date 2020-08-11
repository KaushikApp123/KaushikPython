my_list = ['m','i','n','e','c','r','a','f','t']

print(my_list[2:5])

print(my_list[:-5])

print(my_list[4:])

print(my_list[:])

BuildingGame = {
  "Name": "Minecraft",
  "Developer": "Mojang",
  "yearMade": 2009
}
print(BuildingGame)
ShootingGame = {
  "Name": "CallOfDutyMW",
  "Developer": "Activision",
  "yearMade": 2018
}
print(ShootingGame)
BuildingandShootingGame = {
  "Name": "Fortnite",
  "Developer": "EpicGames",
  "yearMade": 2017
}
print(BuildingandShootingGame)

my_tuple = "Minecraft", "Fortnite"
print(my_tuple)


a , b= my_tuple

print(a)
print(b)
nterms = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence up to",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1



# n1 = 1
# n2 = 1
# print(n1)
# print(n2)
#
# for x in range(10):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print (n3)
