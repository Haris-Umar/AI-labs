stack=[]

def push(value):
    stack.append(value)

def pop(stack):
    if len(stack)==0:
        print("no value:")
    else:
        print(stack.pop())


push(17)
push(7)

print(stack)
pop(stack)
pop(stack)
pop(stack)
