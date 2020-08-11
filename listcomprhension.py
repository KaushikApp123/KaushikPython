
#
# (x, y, z) = [1, 1, 2]
# n=3
#
# for i in range (x+1):
#     for j in range (y+1):
#         for k in range (z+1):
#             if ( (i + j + k)  != n):
#                 print([1, j, k])
#
# print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if ( a + b + c) !=n])


if __name__ == '__main__':
    mylist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameAndScore = (name , score)
        mylist.append(nameAndScore)

grades = []
for newList in mylist:
    if grades.count(newList[1]) == 0:
        grades.append(newList[1])
grades.sort()
if len(grades) >= 1:
    secondGrade = grades[1]
else:
    secondGrade = grades[0]
namesList = []
for student in mylist:
    if student[1] == secondGrade:
        namesList.append(student[0])
namesList.sort()

for name in namesList:
    print(name)
    


