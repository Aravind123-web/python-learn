# dictionary data type
employee = {"name": "Aravind", "role": "devops_enginner", "experience": 4}
print(employee)

# accessing value
employee = {"name": "Aravind", "role": "devops_enginner", "experience": 4}
print(employee["name"])

# keys in dictionary should of immutable datatype
sample_dict = {1: 1, 2: 4, 3: 9, 4:8}
print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 9, 3:45}
print(sample_dict[3])

sample_dict = {1:23, 2: 4, 3: 4}
print(sample_dict[1])

#sample_dict = {[1, 2, 3, 4]:1, 2: 3, 3: 4}
#print(sample_dict[[1, 2, 3, 4]])

"""
Traceback (most recent call last):
  File "C:\devops\daws-76s\repos\python-learn\05_dictionary.py", line 19, in <module>
    sample_dict = {[1, 2, 3, 4]:1, 2: 3, 3: 4}
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

"""

# METHODS

dict_keys = sample_dict.keys() # print all keys
dict_values = sample_dict.values() # print all values
dict_items = sample_dict.items() # print all items
print(dict_keys, dict_values, dict_items)

# what happends if you access a key that is not present inside a dict

sample_dict = {"1":23, 2: 4, 3: 4}
print(sample_dict.get(1)) # None
#print(sample_dict[1]) # error

# how to add a new element in dict

sample_dict = {1: 1, 2: 4, 3: 9}
sample_dict[4]= 10
print(sample_dict)

