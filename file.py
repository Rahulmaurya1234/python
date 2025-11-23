f=open('youtube.txt','w')
try:
  f.write("hello world")
finally:
    f.close()
with open('youtube.txt','w') as f:
    f.write("my name is rahul maurya")
with open('youtube.txt','r') as f:
    content=f.read()
    print(content)