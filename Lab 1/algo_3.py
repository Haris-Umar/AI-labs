arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8,9]
length1 = len(arr1)
length2 = len(arr2)
check = False
for i in range(length1):
    for j in range(length2):
        if arr1[i] == arr2[j]:
            print(f"Same values found in arrays: {arr1[i]}")
            check = True

if check == False:
    print("Same value not found in arrays: ")