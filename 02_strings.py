sample_str = "This is sample string"
print(sample_str)

# How to access individual characters from a string
print(sample_str[10])  # prints the second character of the string

# slicing
sub_str = sample_str[2:7]  # prints the characters from index 2 to 6
print(sub_str)

sub_str = sample_str[:]
print(sub_str)  # prints the entire string

sub_str = sample_str[1:]
print(sub_str)  # prints the string from index 1 to the end

sub_str = sample_str[:5]
print(sub_str)  # prints the string from the beginning to index 4

sub_str = sample_str[::2]
print(sub_str)  # prints every second character of the string

sub_str = sample_str[::-1]
print("Reverse string:", sub_str)  # prints the string in reverse order

len_str = len(sample_str)  # prints the length of the string
print("Length of the string:", len_str)

# string methods
# capitalize method
simple_str = "hello"
print(simple_str.capitalize())  # prints the string with the first character capitalized

# split(), join(), format(), count(), strip(), lstrip(), rstrip() methods

#split() method splits the string into a list of words based on the specified delimiter (default is whitespace)
sample_str = "This is a sample string"
str_split = sample_str.split()  # splits the string into a list of words
print(str_split, type(str_split))

#join() method joins the elements of a list into a single string using the specified delimiter
join_split_str = " ".join(str_split)  # joins the list of words into a single string with space as delimiter
print(join_split_str, type(join_split_str))

#count() method counts the number of occurrences of a substring in the string
count_a = sample_str.count("a")  # counts the number of occurrences of "a" in the string
print("Count of 'a' in the string:", count_a)

#strip() method removes the leading and trailing whitespace characters from the string
sample_str = "      I want to clear the devops interview        "
strip_str = sample_str.strip()  # removes the leading and trailing whitespace characters
print("String after strip():", strip_str)

# string are immutable
sample_str = "This is a sample string"
sample_str[-1] = "G"  # This will raise an error because strings are immutable in python
print(sample_str)

"""
Traceback (most recent call last):
  File "C:\devops\daws-76s\repos\python-learn\02_strings.py", line 56, in <module>
    sample_str[-1] = "G"  # This will raise an error because strings are immutable in python
    ~~~~~~~~~~^^^^
TypeError: 'str' object does not support item assignment

"""




