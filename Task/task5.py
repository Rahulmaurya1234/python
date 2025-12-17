# TASK 5: List Handling (Mutable bug avoid)

# 👉 Ek list lo:

# nums = [1, 2, 3, 4, 5]


# sirf odd numbers ki new list banao

# original list change nahi honi chahiye

list=[1,2,3,4,5]
# print(list)l=list.copy()
l=[]
for i in list:
   print(i)
   if i%2 != 0 :
      l.append(i)
      
print(l)
      


