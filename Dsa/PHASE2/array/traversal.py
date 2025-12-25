# # Array ke har element pe ek-ek karke jaana


# arr=[1,2,4,5,6,7,8,8]
# for i in arr:
#     print(i)


# for i in range(len(arr)):
#     print(arr[i])


# #complexity:o(n)

arr=[10,20,30,40,50,60,70,80]
  
def second_largest(arr):
    second_largest=arr[0]
    largest=arr[0]
    for i in arr:
       if largest < i:
           second_largest=largest
           largest=i
       elif largest > i and i > second_largest:
           second_largest=i

    return second_largest
print(second_largest(arr))