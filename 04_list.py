# create list
# we can define []
sample_list = ["linux", "terraform", "ansible", "k8s"]
print(sample_list)

# indexing, slicing

sample_ele = sample_list[2] # Accessing the third element of the list
print(sample_ele)

sliced_list = sample_list[1:3] # Slicing the list from index 1 to 2
print(sliced_list)

sample_ele = sample_list[-1] # Accessing the last element of the list
print(sample_ele)


sliced_list_len = len(sliced_list) # Getting the length of the sliced list
print(sliced_list_len)

# list is a mutable data type, meaning once we defined, it can be modified, added, or removed.
sample_list[1] = "shell" # Modifying the second element of the list
print(sample_list)

# Append/add an element to the end of the list
# append means added each new element in one item

sample_list = ["linux", "terraform", "ansible", "k8s"]
sample_list.append("shell") # Adding an element to the end of the list. This is inplace operation, meaning it modifies the original list.
print(sample_list)

sample_list_new = ["linux", "terraform", "ansible", "k8s"]
#sample_list_new = ["devops", "aws", "docker"]
sample_list.append(sample_list_new)
print(sample_list)


# Append list to list
# sample_list.append(sample_list)
# print(len(sample_list)) # ['linux', 'terraform', 'ansible', 'k8s', 'shell', [...]]
# last_ele = sample_list[-1]
# print(last_ele)

# extend
# extend means each element is added spearatly 
sample_list = [1, 2, "sample", True]
sample_list.extend(sample_list)
print(len(sample_list), sample_list)

# membership operator
# in operator
sample_list = [1, 2, "sample", True]
print(2 in sample_list)
print(3 in sample_list)

# not in operator
sample_list = [1, 2, "sample", True]
print(3 not in sample_list)
print("sample" not in sample_list)

is_ele = 2 in sample_list
print(is_ele)
               





