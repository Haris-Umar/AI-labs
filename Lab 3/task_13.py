x = input("Enter String: ")
d = 0
a = 0
for i in x:
    if i.isdigit():
        d = d + 1
    elif i.isalpha():
        a = a + 1

print("Digits: ",d)
print("Letters: ",a)