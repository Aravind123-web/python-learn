# example:1 Check whether the given number is greater than or not

user_input = int(input("Enter a number:")) # ouput comes in sting datatype
#user_input = int(user_input) # converting string to integer

if user_input > 10:
    print("User input value is greater than 10")
else:
    print("User input value is less than or equal 10")

# example:2 Check whether the given number is equal to 10 or 
# greater than 10 or 
# less than 10 or something else

# method 1 Nested if-else
if user_input == 10:
    print("right on target")
else:
    if user_input > 10:
        print("User unput value is greater than 10")
    else:
        if user_input < 10:
            print("User input value is less than 10")

# method 2
if user_input == 10:
    print("right on target")
elif user_input > 10:
    print("user input value is greter than 10")
else:
    print("user input value is less than 10")
    
# Exception handlinhg: try - except
# see below example of exception handling. if user given valid input like (1 2 3 4)
# means it will execute the try code
# if in valid the input value like string(a,s,d,f,) it won't excute try code, it will excute except code
   
try:
    user_input = int(input("Enter a number:"))
    if user_input == 10:
        print("Right on target")
    elif user_input > 10:
        print("User input value is greater than of 10")
    else:
        print("User input value is less than of 10")
except ValueError:
    print("Please enter a number")

