# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re

def isValidPhoneNumber(phoneNum):
    rePhoneNumber = r"[789]{1}[0-9]{9}$"
    if (re.match(rePhoneNumber, phoneNum)):
        return "YES"
    else:
        return "NO"

# result = ["yes","no","yes"]
# for x in range(int(input())):
#     result.append(isValidPhoneNumber(str(input())))
result = [isValidPhoneNumber(str(input())) for x in range(int(input()))]
print("\n".join(result))

