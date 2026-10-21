# Type conversion
# it means converting value from one data type to another data type
# 1. convert string to list
sample_str = "This is a sample string"
sample_str_list = list(sample_str)
print("list data type:", sample_str_list)

# 2. convert string to tuple
sample_str_tuple = tuple(sample_str)
print("tuple data type:", sample_str_tuple)

# 3. convert string to set
sample_str_set = set(sample_str)
print("set data type:", sample_str_set)

# Accept input from user
# By default user input cominig from string, we need to convert as what is required datatype

user_input = input("Enter a number:")
print(user_input, type(user_input))
"""
Enter a number:12
12 <class 'str'> # by default it is a string 
"""
#add_10 = int(user_input) + 10
#print(add_10)

"""
Traceback (most recent call last):
  File "C:\devops\daws-76s\repos\python-learn\07_type_converstion.py", line 25, in <module>
    add_10 = int(user_input) + 10
             ~~~^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '12 23 44 554'

"""