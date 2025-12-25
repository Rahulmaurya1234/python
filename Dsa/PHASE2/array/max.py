# Min / Max Element

def find_min(arr):
   mini=arr[0]
   for i in arr:
      if mini>i:
         mini=i
   print(mini)
    
         
           
def find_max(arr):
    maxi=arr[0]
    for i in arr:
       if maxi<i:
         maxi=i
    print(maxi)
         
      

arr=[1,64,49,0,5,6,7]
find_min(arr)

find_max(arr)

# print(min(arr))
# print(max(arr))
