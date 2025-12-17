# TASK 8: Generator (IMPORTANT)

# 👉 Generator likho jo:

# 1 se 50 tak

# sirf multiples of 5 yield kare

def multiples_of_5():
    for number in range(1, 51):
        if number % 5 == 0:
            yield number

for x in multiples_of_5():
    print(x)
