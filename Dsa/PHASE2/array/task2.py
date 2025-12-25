# # # 🔥 Task-2

# # # Find second largest element

# # arr=[1,2,3,4,4,5,56,9,87676,0,45465,345678]
# # def find_secondlarge(arr):
# #     max1=arr[0]
# #     second=[]
# #     for i in range(len(arr)):
# #         if arr[i]>max1 :
# #             max1=arr[i]
# #             second.append(max1)
            
    
# #     return second[len(second)-1-1]

# # print(find_secondlarge(arr))
# arr=[1,5,7,3,8,9]
# max=arr[0]
# i=0
# j=len(arr)
# while i<j:
#     if arr[i]>max:
#         max=arr[i]
#     elif arr[j-1]>max:
#         max=arr[j-1]
#     j-=1
#     i+=1
# print(max)  



# arr=[1,5,7,3,8,9]
# m=arr[0]
# n=arr[0]
# for i in arr:
#     n=m
#     if i > m:
#         m=i
# print(n)






# arr=[10,20,30,40,50,60,70,80]
arr=[53,45,6,0,0,0,3,2,4565,666,7777]
largest=arr[0]
second=arr[0]
for i in arr:
        if largest < i:
            second=largest
            largest=i
        elif largest > i and i > second:
              second=i

print(second)