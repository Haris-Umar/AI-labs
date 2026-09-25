r = int(input("Enter row: "))
c = int(input("Enter column: "))

m = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(i * j)
    m.append(row)

print(m)