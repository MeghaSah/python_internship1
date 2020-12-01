# # PROBLEM 1
# #divide by zero
# try:
#     print(9/0)
# except:
#     raise Exception("numbers cant be divisible by zero")
#
# # array index error
# l = [1,2,3,4,5]
# try:
#     print(l[7])
# except:
#     print("array's index is out of bound exception")
#
# # type error
# sstr = "cyber:"
# try:
#     sstr[0]='h'
# except:
#     raise Exception("string types are immutable")
#
# # name error
# a = "security"
# try:
#     print(b)
# except:
#     print("Name is not defined")
# else:
#     print("end of the code")





# # PROBLEM 2
# try:
#
#     n1 = int(input("Enter First Number: "))
#     n2 = int(input("Enter Second Number: "))
#     operator = input("Enter Arithmetic Operator: ")
#
#     if operator == '+':
#
#         print(n1, "+", n2, "=", n1 + n2)
#
#     elif operator == '-':
#
#         print(n1, "-", n2, "=", n1 - n2)
#
#     elif operator == '*':
#
#         print(n1, "*", n2, "=", n1 * n2)
#
#     elif operator == '/':
#
#         try:
#
#             print(n1, "/", n2, "=", n1 / n2)
#
#         except ZeroDivisionError:
#
#             print("/ by zero")
#
#     elif operator == '%':
#
#         print(n1, "%", n2, "=", n1 % n2)
#
#     else:
#
#         print("Invalid Operator")
#
# except:
#
#     raise Exception("Invalid Input")



# # PROBLEM 3
# try:
#     print(value)
# except NameError:
#     print("value is not defined")
# except:
#     raise Exception(self)
#
#
# # PROBLEM 4
# When the input is perfect,clear and as per the requirement then at the time ,we can ignore the try-except block.


# PROBLEM 5
try:
    a = int(input())
    print(a)
except:
    raise Exception("Value is not defined")




