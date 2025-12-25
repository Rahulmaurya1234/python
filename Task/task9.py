# TASK 9: Input Trap Handling

# 👉 User se input lo:
l=(input("enter num").split())
print(l)
nums=[]
for i in l:
    try:
        nums.append(int(i))
    except:
        pass
print(nums)
