x = input("Enter Password: ")
uc = lc = num = symbol = 0
for i in x:
    if i.isdigit():
        num = True
    elif i.islower():
        lc = True
    elif i.isupper():
        uc = True
    elif i in "$#@":
        symbol = True

if uc and lc and num and symbol and 6 <= len(x) <= 16:
    print("Valid Password: ")
else:
    print("InValid Password: ")