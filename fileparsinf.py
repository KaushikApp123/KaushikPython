# def parseLine(line):
#     pairs = line.split(", ")
#     myDictionary = {}
#     for pair in pairs:
#         (key, value) = pair.split("=")
#         myDictionary[key] = value
#     return myDictionary
#
# myList = []
# myFile = open("testData.txt", "r+")
# lines = myFile.readlines()
# for line in lines:
#     lineResult = parseLine(line.replace("\n", ""))
#
#     myList.append(lineResult)
#
# print(myList)
#


hello = "hello"
x = hello[:4] + "WW" + hello[4:]
print(x)