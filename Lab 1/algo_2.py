x = int(input("Enter number: "))
check = False
arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8,9]
length1 = len(arr1)
length2 = len(arr2)
for i in range(length1):
    if arr1[i] == x:
        print("Value found in array 1: ")
        check = True

for i in range(length2):
    if arr2[i] == x:
        print("Value found in array 2: ")
        check = True

if check == False:
    print("Value not found in arrays")