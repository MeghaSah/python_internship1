# add +2 to every value to elements
num= [1, 2, 3, 4, 5]
result = []
for i in range (0,len(num)):
    result.append(num[i] + 2)
print("result:" +str(result))

# write a program in given pattern
# 54321
# 4321
# 321
# 21
# 1
for i in range(5,0,-1):
    for j in range (i,0,-1):
        print(j, end="")
    print()

# program to print fibonacci sequenc
def fibbo(n):
    if n <= 1:
        return n
    else:
        return(fibbo(n-1) + fibbo(n-2))
n = int(input("no of terms:"))

if n <= 0:
    print("please enter a positive integer")
else:
    print("fibonacci sequence:")
    for i in range(n):
        print(fibbo(i))




# Python program to check if the number is an Armstrong number or not
num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


#Multiplication table of 9 in Python

num = 9
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# tto check number is positive or negative
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
else:
   print("Negative number")


#convert days to ages


no_of_days = int(input())

if (no_of_days % 365 == 0):

    print(f"{no_of_days} Days = ", no_of_days // 365, "Year")

else:

    year = no_of_days // 365

    remaining_days = no_of_days % 365

    print(f"{no_of_days} Days = ", year, "Year", f"{remaining_days} Days")

# solve trignometric function
import math as mt

print(mt.sin(90),mt.cos(30))

# basic airthmetic calculator
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
operator = input("Enter Arithmetic Operator: ")


if operator == '+':

    print(n1, "+", n2, "=", n1 + n2)

elif operator == '-':

    print(n1, "-", n2, "=", n1 - n2)

elif operator == '*':

    print(n1, "*", n2, "=", n1 * n2)

elif operator == '/':

    print(n1, "/", n2, "=", n1 / n2)

elif operator == '%':

    print(n1, "%", n2, "=", n1 % n2)

else:

    print("Invalid Operator")


