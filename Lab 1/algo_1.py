x = int(input("Enter number: "))
check = False
arr = [1,2,3,4,5]
length = len(arr)
for i in range(length):
    if arr[i] == x:
        print("Value found in array: ")
        check = True
if check == False:
    print("Value not found in array")