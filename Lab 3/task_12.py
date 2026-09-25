x = input("Enter binary: ").split(",")
for i in x:
    if int(i,2) % 5 == 0:
        print(i)
