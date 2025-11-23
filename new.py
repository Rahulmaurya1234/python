nums = [4, 1, 7, 2]
nums.sort()
print(nums)     # [1, 2, 4, 7]


nums.sort(reverse=True)
print(nums)     # [7, 4, 2, 1]

text = "hello world"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
name = "   Rahul   "
print(name.strip())      # "Rahul"
sentence = "I love Python"
words = sentence.split()     # space ke hisaab se todta hai
print(words)                 # ['I', 'love', 'Python']
