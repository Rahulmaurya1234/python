# # arr reverse
# arr=[1,23,4,5,6,6,77,88]
# print(arr[::-1])
# rev=[]
# for i in arr:
#     rev.insert(0,i)
# print(rev)
    
    
# # string reverse
# str = "rahul"
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)





# Task-3

# Reverse array without slicing



arr=[1,2,3,4,5,6,7]
rev=[]
# for i in arr:
#     rev.insert(0,i)
# print(rev)


for i in range(len(arr)):
    n=(len(arr)-1-i)

    rev.append(arr[n])
print(rev)