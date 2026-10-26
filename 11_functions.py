# function defination we can represent a keyword "def"
# def sample_func():
#     print("This is basic sample function")

# # call the function
# sample_func()

# def add(num_1, num_2):
#     """
#     This function performs addition of 2 numbers
#     """
#     res = num_1 + num_2
#     return res
# # call the function
# #res = add(1,2)
# res = add(num_2 = 1, num_1 =2)
# print(res)

# help(add)

# default parameters

# def add(num_1, num_2, num_3 = 20):
#     res = num_1 + num_2 + num_3
#     return res
# # call the function
# res = add(num_2= 1, num_1= 2)
# print(res)


# A: varible length arguments
# one user enters 10 numbers and another user enters 100 numbers.
# define your function to handle this situation

# def add(*nums):
#     res = sum(nums)
#     return res
# # call the function
# res = add(1, 2, 3)
# print(res)
# res = add(1, 2, 3, 4, 5, 6)
# print(res)

# variable arguments

# def add(num_1, num_2, *args):
#     res = num_1 + num_2 + sum(args)
#     return res
# # call the function
# res = add(1, 2, 3)
# print(res)
# res = add(1, 2, 3, 4, 5, 6)
# print(res)

# keywordarguments (kwargs)

def add(*args, **kwargs):
    print(args, kwargs)
    
# call the function
res = add(1, 2, 3)
print(res)
res = add(1, 2, 3, num_1=4, num_2 =5, num_3=6)
print(res)

# lambda: inline function

add_numbers = lambda num1, num2: num1 + num2
res = add_numbers(1, 2)
print(res)