arr = [1,2,3,4,5,3,7,8]
check = False
length = len(arr)
for i in range(length):
    for j in range(i+1,length):
        if arr[i]==arr[j]:
            print("Duplicate value found in array: ")
            check = True
if check == False:
    print("No duplicate value in string: ")
