# create python module with list and import th module in another .py file and chnage the value in list
import mymodule
LIST = [x+1 for x in mymodule.LIST]
print(LIST)

# install pandas package and try to import the package in a python file
import pandas as pd
num = [10,20,30,40]
num2 =pd.Series(num)
print(num2)

# import a module that picks a random number and write a program to fetch a random number from 1 to 100 on every run
import random
print(random.randint(0,100))

# import sys package and find the python path
import sys
print(sys.path)

# try to install a package and uninstall a package using pip
pip install pandas
pip uninstall pandas