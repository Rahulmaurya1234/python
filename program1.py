# Given two numbers num1 and num2.
#  The task is to write a Python program to find the addition of these two numbers. 


#  normal methode


# num1=int(input("enter the first number:"))
# num2=int(input("enter the seccond nummber:"))
# sum = num1 + num2
# print("sum of the two numbers is :",sum)

# # using function

# # def add(num1,num2):
#     return num1+num2
# num1=int(input("enter the first number:"))
# num2=int(input ("entr the second number: "))
# print("sum of the tow number is : " , add(num1,num2))

# using lembda function

sum=lambda x,y : x+y
x=3
y=8
z=sum(x,y)
print(z)

# # Define a lambda function to add two numbers
# add_numbers = lambda x, y: x + y
# Define a lambda function to add two numbers
add_numbers = lambda x, y: x + y

# Take
# Take input from the user
num1 = 1
num2 = 2

# Call the lambda function to add the two numbers
result = add_numbers(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is", result)


# Python3 program to add two numbers

num1 = 15
num2 = 12

# Adding two nos
import operator
su = operator.add(num1,num2)

# printing values
#print("Sum of {0} and {1} is {2}" .format(num1,
 #                                      num2, su))
print(su)


# add two num by recursion

def add (x,y):
    if  y==0:
        return x
    else:
        return add(x+1,y-1)
x=488
y=45
z=add(x,y)
print(z)


