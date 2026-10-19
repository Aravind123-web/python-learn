# Tuple in Python
# There are two methods to create a tuple
# 1. ()
# 2. tuple()
# Behavior: They are immutable, meaning that once a tuple is created, its elements cannot be changed, added, or removed.
from inspect import Traceback
from operator import index


sample_tuple = ("linux", "terraform", "ansible", "k8's") # Tool set
print("List of devops tool:" + str(sample_tuple))

sample_ele = sample_tuple[1] # Accessing the second element of the tuple
print(sample_ele)

sample_ele = sample_tuple[-1]
print(sample_ele)

# slicing
sliced_tuple = sample_tuple[1:3]
print(sliced_tuple)

sliced_tuple_len = len(sliced_tuple)
print(sliced_tuple_len)

# Immutable
#sample_tuple[1] = "shell_script" # This will raise an error because tuples are immutable in python
#print(sample_tuple)

"""
Traceback (most recent call last):
  File "C:\devops\daws-76s\repos\python-learn\03-tuple.py", line 23, in <module>
    sample_tuple[1] = "shell_script" # This will raise an error because tuples are immutable in python
    ~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment

"""

# operations

res_tuple = sample_tuple + sliced_tuple # concatenation of two tuples
print(res_tuple) # ('linux', 'terraform', 'ansible', "k8's", 'terraform', 'ansible')

res_tuple_1 = sliced_tuple * 3 # create a new tuple by repeating the elements of the original tuple
print(res_tuple_1) # ('terraform', 'ansible', 'terraform', 'ansible', 'terraform', 'ansible')

# Methods


k8s_idx = res_tuple.index("k8's") # returns the index of the first occurrence of the specified value
print(k8s_idx) # 3

# Tuple unpacking
linux, terraform, ansible, k8s = ("linux", "terraform", "ansible", "k8's") # unpacking the tuple into individual variables
print(linux, terraform, ansible, k8s) # linux terraform ansible k8's

linux, *tools, orchestration = (linux, "terraform", "ansible", "k8's") # unpacking the tuple into individual variables with * operator
print(linux, tools, orchestration) # linux ['terraform', 'ansible'] k8's
print(*tools) # terraform ansible k8's