# def evengenerater(n):
#     for i in range (2,n+1,2):
#         yield i
# for even in evengenerater(20):
#     print(even)



# def factorial(n):
#     if(n<1):
#         return 1
#     else:
#             return n*factorial(n-1)
         
# print(factorial(5))



def factorial(n):
    result=1
    if n<1:
        return 1
    else:
        for i in range(n,0,-1):
            result=result*i
        return result
print(factorial(5))