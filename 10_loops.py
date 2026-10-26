# 1. how to access element by element
sample_list = ["linux", "docker", "terraform", "k8s", "shell"]
# lenght of sample list
# len_sample_list = len(sample_list)
# print("length of sample list: ", len_sample_list)
# for ele in sample_list:
#     print(ele, len(ele))

# 2. Print the element and its correspoding index by using enumerate built function
# for idx, ele in enumerate(sample_list):
#     print(idx, ele)

# 3. Print the element and its correspoding index by using range based for loop
# range based for loop
# ex: 1:10 -> 1,2,3,....9 (last one is excluded)
#sample_range= range(0, len(sample_list))
#print(sample_range, type(sample_range))
#for idx in sample_range:
#    print(idx)

# for idx in range(0, len(sample_list)):
#     print(idx, sample_list[idx])
#idx → gives the index number
#sample_list[idx] → gives the element at that index

# cotinue statment in for loop. it means skip the current statement

# for idx in range (0, len(sample_list)):
#     if sample_list[idx] == "k8s":
#         continue
#     print(idx, sample_list[idx])

# # break statement 
# for idx in range (0, len(sample_list)):
#     if sample_list[idx] == "k8s":
#         break
#     print(idx, sample_list[idx])


##############################################################################
# while loop
sample_list = ["linux", "docker", "terraform", "k8s", "shell"]

# break stament
idx = 0
while idx < len(sample_list):
    if sample_list[idx] == "k8s":
        break
    print(idx, sample_list[idx])
    idx += 1 # increment operator

# take dict datatype
sample_dict = {1:"a", 2:"r", 3:"v"}
for k, v in sample_dict.items():
    print(k, v)



