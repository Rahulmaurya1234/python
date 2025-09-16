# Python Program to Find LCM of Two Numbers

# def lcm(x, y):
#     # Choose the greater number
#     if x > y:
#         greater = x
#     else:
#         greater = y

#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1

#     return lcm

# # Example usage
# num1 = 54
# num2 = 24

# print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))


# # Find LCM of Two Numbers Using the GCD (Greatest Common Divisor)


# import math

# def lcm_using_gcd(a, b):
#     gcd = math.gcd(a, b)
#     lcm = (a * b) // gcd
#     return lcm

# # Example usage:
# num1 = 12
# num2 = 15
# print("LCM of", num1, "and", num2, "is:", lcm_using_gcd(num1, num2))



def LCM(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i

# Driver program to test above function
if __name__ == '__main__':
    a = 12
    b = 15
    print("LCM of", a, "and", b, "is", LCM(a, b))
