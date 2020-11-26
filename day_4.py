# write a prrogram to create a list of n integer values and add an tem to the list
numbers = [1,2,3,4,5,6]
numbers.append(7)
print(numbers)

#delete the item from the list
numbers.remove(5)
print(numbers)

# storing largest number to the list
largest = max(numbers)
print(largest)

# storing smallest number to the list
smallest = min(numbers)
print(smallest)

# create  a tuple and print the reverse of the created tuple
tuple = ('a','b','c','d','e')

def Reverse(tuple):
    new_tuple = tuple[::-1]
    return new_tuple
print(Reverse(tuple))

# create a tuple and convert tuple into list
tup = ('ram','shyam', 'hari', 'mohan', 'rahul')
print(list(tup))