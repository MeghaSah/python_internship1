# problem 1
a = int(input("enter 1st num:"))
b = int(input("enter 2nd num:"))
def add(a,b):
    sum = a+b;
    return sum
print("The addition of two number is" , add(a,b))

def sub(a,b):
    diff = a-b;
    return diff
print("The subtraction of two number is" , sub(a,b))

def mul(a,b):
    multiply = a*b;
    return multiply
print("The multiplication of two number is" , mul(a,b))

def div(a,b):
    division = a/b;
    return division
print("The division of two number is" , div(a,b))


#problem 2
def COVID( patient_name, body_temp = 98):
    print("Patient's Name:",patient_name)
    print("Patient's Body Temperature:",body_temp)
COVID("MEGHA")