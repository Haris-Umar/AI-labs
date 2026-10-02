value = [1,21,13,40,5,16,117,28,9]
value.sort()
print(value)
x = int(input("Enter Value to search its index: "))

left = 0
right = len(value)-1
found = -1
while left <= right:
    mid = ( left + right ) // 2
    if value[mid] == x:
        found = mid
        break
    elif value[mid] > x:
        right = mid - 1
    elif value[mid] < x:
        left = mid + 1

if found != -1:
    print(f"Value found at {found} index")
else:
    print("Value not found: ")