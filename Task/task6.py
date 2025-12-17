# TASK 6: Dictionary Frequency

# input:text = "machinelearning"

#output {'m':1, 'a':2, 'c':1, ...}

text = "machinelearning"
# print(text)
dic={}

for ch in text:
  if ch in dic:
    dic[ch]+=1
  else:
    dic[ch]=1
print(dic)