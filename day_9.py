 problem 1
my_list = [1,2,3,4,5]
y = 2
print(list(map(lambda x:x*y,my_list)))

# problem 2
from functools import reduce
fib = lambda n: reduce(lambda x,_x:x+[x[-1]+ x[-2]],range(n-2),[0,1])
print(*fib(int(input())))

# problem 3
n = int(input())
my_list = list(map(int,input().split()))
print(map(lambda x : x*n, my_list))

# problem 4
mylist = [1,3,9,18,20,27,30,36]
print(*filter(lambda x : x%9 == 0, mylist))

# problem 5
list1 = [1,2,3,4,5,6,7,8]
print(len(list(filter(lambda x : x%2 == 0, list1))))