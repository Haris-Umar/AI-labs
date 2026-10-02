queue = []

def push(value):
    queue.append(value)

def pop(queue):
    if len(queue) == 0:
        print("No value: ")
    else:
        print(queue.pop(0))

push(17)
push(11)
print(queue)
pop(queue)
print(queue)
push(10)
pop(queue)
pop(queue)
pop(queue)
pop(queue)