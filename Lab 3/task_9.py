a = 1
b = 1
while a < 50:
    print(a,end=" ")
    temp = a
    a = b
    b = temp+a

# next part fizzbuzz
for i in range(51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)