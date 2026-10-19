# This is a simple python script
"""
This is a multi-line comment
"""
# Define a variable
a = 5
# print the value that is stored in the variable
print(a)
# strings
b = 'this is string'
c = "this is also a string"
d = """this is a multi-line string"""

# Today's weather is nice
b = 'Today\'s weather is nice'
print(b)
b = "Today's weather is nice"
print(b)

# float variable
e = 5.48
print(e)

# boolean variables
f = False
g = True
print(f)
print(g)

# python special datatypes
"""
- List
- Tuple
- Set
- Dictionary
"""

# This is list
Test_List = ["hello", "world", "python"]
print(Test_List)

# This is tuple
Test_Tuple = ("hello", "world", "python")
print(Test_Tuple)

# This is set
# consider the value in an arbitrary way
Test_Set = {"hello", "world", "python"}
print(Test_Set)

#This is dictionary
# dictionary is a collection of key-value pairs
Test_Dict = {'a': 1, 'b': 2, 'c': 3}
print(Test_Dict)

#type() function is a inbuilt function in python, it prints the datatype of the variable
print(type(Test_Dict))
print(type(print))
print(type(Test_Tuple))
#opeartions
#Add
#Sub
#Mul
#Div
#Integral Division
#Module Division

a = 10
b = 3
c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(e)

f = 12
g = 10
h = f / g
print(h)

# power
k = 2
print(k**2)
# comparison operators
a = 10
b = 20
res = a > b
res_1 = a < b
res_2 = a != b # not equal to
res_3 = a == b # equal to
print(res, res_1, res_2, res_3)

# logical operators
# AND, NOT, OR

a = True
b = False
res = a and b
res_1 = a or b
res_2 = not a
res_3 = not b
print(res, res_1, res_2, res_3)