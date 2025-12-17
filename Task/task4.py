# TASK 4: String Analysis

# 👉 Input string lo aur print karo:

# total characters

# vowels count

# consonants count

# 📌 Hint: isalpha()

str=input("enter string : ")

print(str.isalpha())
#print string

print("string:",str)

#totle characters 

print("totle characters:",len(str))

#vowels count
v=0
c=0
for ch in str:
    if ch == "a" or ch == "e"  or ch == "o"  or ch == "u"  or ch == "i" :
        v+=1
    else:
        c+=1
print("vowels:",v,"consonent",c)


# print("charaters:",c,"vowels:",v)


