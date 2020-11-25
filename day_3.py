# write python script to merge two python dictionaries
students_name = {
    1: 'michel',
    2: 'charlie',
    3: 'john',
    4: 'smith'
}
new_students = {
    5: 'aditi',
    6: 'jahnvi',
    7: 'tanmay',
    8: 'rahul'
}
students_name.update(new_students)
print(students_name)

# write a python program to remove a key from dictionary
students_name.pop(4)
print(students_name)

# write a python program to map two lists into a dictionary
list1 = [1,2,3,4,5]
list2 =['one', 'two', 'three', 'four', 'five']
numbers = dict(zip(list1,list2))
print(numbers)

# write a program to find a length of a set
programming_languages = {'c++', 'java', 'python', 'javascript'}
print(len(programming_languages))

# write a python program to remove the intersection of 2nd set from the 1st set
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {4,5,6,7,8,99,87}
print(set2-set1)