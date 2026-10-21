# sets data type
# it is mutable datatype
# set is a collection of unique values
# do not allow duplicates
# A set return unique elements that is stored inside that variable
# sets don't consider the order of insertion
# sets don't supporting indexing
sample_set = {3, 2, 4, 5, 4, 1}
print(sample_set)

# Add elemets to set
sample_set = {3, 2, 4, 5, 4, 1}
sample_set.add(23)
print(sample_set)
#print(sample_set[3]) #sets don't supporting indexing
"""
Traceback (most recent call last):
  File "C:\devops\daws-76s\repos\python-learn\06_sets.py", line 15, in <module>
    print(sample_set[3])
          ~~~~~~~~~~^^^
TypeError: 'set' object is not subscriptable
"""
#set opeartions like intersection(), union()
