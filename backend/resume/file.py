skills="i have good skills in python programming"
with open("skille.txt","r") as f:
    data = f.read()
    data = data.splitlines()
    for line in data:
        if line in skills:
            print(f"{line}: present")
        else:
            print(f"{line}: not present")

    