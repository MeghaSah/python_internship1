# program using zip() function and list() function, create a merged list of tuples from the twolists given
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list(zip(list1,list2)))

# first create a range from 1-8. then using zip,merge the given  list and range together to create a new list of tuples
list3 = [i for i in range(1, 9)]
list4 = list(map(int, input().split()))
print(list(zip(list3, list4)))

# using sorted() function ,sort the list in ascending order
list5 = [5, 6, 7, 4, 3, 2, 7, 8]
print(sorted(list5))

# python program using filter function , filter the even numbers so that only numbers are passed to the new list
list6 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(list(filter(lambda x:x%2,list6)))