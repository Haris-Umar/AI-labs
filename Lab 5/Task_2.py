class PriorityQueue:

    def __init__(self):
        self.items = []                  # each entry is [priority, item]

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item, priority, length):
        if len(self.items) >= length:    # length passed as parameter
            print("Queue is full.")
            return
        index = 0
        while index < len(self.items) and self.items[index][0] <= priority:
            index += 1
        self.items.insert(index, [priority, item])

    def pop(self):
        first = self.items[0]            # smallest number = highest priority
        del self.items[0]
        return first

    def display(self):
        while not self.is_empty():
            priority, item = self.pop()
            print(f"{item} (priority {priority})")


pq = PriorityQueue()

n = int(input("How many items: "))

print(f"Enter {n} items: ")
for i in range(n):
    item = input(f"Item {i + 1}: ")
    priority = int(input(f"Priority of {item}: "))
    pq.push(item, priority, n)           # pass length here

print("\nItems in priority order:")
pq.display()