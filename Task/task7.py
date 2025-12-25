# TASK 7: Function + Return

# 👉 Function likho:

# list input le
#isinstance(value, datatype)

# square of even numbers return kare
def fun(l):
    list=[]
    for i in l:
        if isinstance(i, int):
            if  i%2==0:
                list.append(i*i)
            else:
                pass
        else:
            pass

    return list


l=[1,2,3,4,5]
print(fun(l))
    