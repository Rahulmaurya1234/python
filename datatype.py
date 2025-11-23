
# data define lik as which type of values store in variables 

# Number = integer. float.  complex


# number=44
# print(number)

# a= 5.9
# print(a)

# z=5 + 4j
# print(z.real)
# print(z.imag)


# print(type(a))
# print(type(number))
# print(type(z))


# string type data types

# name = "Rahul"
# msg = 'Hello'
# info = "Python 3.12"

# print(name)
# print(msg)
# print(info)



# boolean

# is_adult=True
# is_student=False

# print(5>4)
# print(3>5)

# list – List (Ordered Collection)

# Definition:
# List ek ordered, changeable (mutable) collection hoti hai.
# Isme multiple values store kar sakte ho, square brackets [] ke andar.

# list=[3,4,5.3,"rahul",5.3]
# print(list)
# list[0]=11
# print(list)
# list.append(12)
# print(list)
# list.insert(1,23)
# print(list)
# list.remove(23)
# print(list)

# # # Indexing & slicing:

# # print(list[0])
# # print(list[1:4:1])


# # Indexing → ek ghar ka address

# # numbers[2] → 3rd element

# # Slicing → ek gali ka range

# # numbers[1:4] → 2nd se 4th ghar tak (last wala exclude)

# name="rahul"
# print(name[3])
# print(len(name))
# name[0]=k






# tuple – List jaisa, but change nahi hota (immutable)
# Definition

# Tuple ek ordered collection hai jisme multiple values store kar sakte ho,
# lekin banne ke baad usko change nahi kar sakte.

# Syntax: () parentheses

# Ordered: ✅

# Changeable (mutable): ❌ (not changeable)

# numbers = (10, 20, 30)
# print(numbers[0])      # 10
# print(numbers[1:3])    # (20, 30)


# set – Unique values, order fix nahi
# Definition

# Set ek unordered collection of unique items hai.

# Syntax: {} curly braces

# Ordered: ❌

# Changeable: ✅ (items add/remove ho sakte hain)

# Duplicate values: ❌ (automatically hat jati hain)


# nums = {1, 2, 3, 3, 2}
# print(nums)     # {1, 2, 3}  (duplicates gayab)


# Set me indexing nahi hoti:

# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a | b)   # union: {1, 2, 3, 4, 5}
# print(a & b)   # intersection: {3}
# print(a - b)   # difference: {1, 2}


# dict – Dictionary (key → value pairs)
# Definition

# Dictionary me data key–value pairs ke form me store hota hai.

# Syntax: {key: value}

# Key unique hoti hai

# Values kuch bhi ho sakti hain

# Ordered (Python 3.7+): ✅


# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }

# print(student["name"])   # Rahul
# print(student["age"])    # 20
# student["age"] = 21
# student["city"] = "Mumbai"
# print(student)
# del student["course"]
# print(student)


# print(student.keys())    # dict ke saare keys
# print(student.values())  # saari values
# print(student.items())   # (key, value) pairs




# None – No value / Empty
# Definition

# None ek special value hai jo batati hai:

# “Yaha koi value hi nahi hai”
# ya
# “Value abhi decide nahi hai”

# Type: NoneType

# Sirf ek hi value: None


# x = None
# print(x)          # None
# print(type(x))    # <class 'NoneType'>

# def add(a, b):
#     print(a + b)   # sirf print, return nahi

# result = add(2, 3)   # prints 5
# print(result)        # None



nums = [1, 2, 2, 3, 4, 4]
s = set(nums)
print(s)
