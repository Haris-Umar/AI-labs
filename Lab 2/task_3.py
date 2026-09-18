def func_1():
    print("First Function")

x=1
if x>0:
    func_1()

# function parameters

def my_name(name):
    print("My name"+" "+name)

def classmate_name(name):
    print("Class mate name"+" "+name)

my_name("Haris")
classmate_name("Ahmad")

# default parameter
def default(name="Haris"):
    print("Name "+""+name)

default()
default("ALI")

# list function
def list(x):
    for i in x:
        print(i)

l = [1,2,3,4,5]
list(l)

# return value
def add(a,b):
    return a + b

res = add(12,5)
print(res)

def dif_type(depart,sem):
    print("DEPARTMENT: "+""+ depart +" "+"Semster: "+""+ str(sem))

dif_type("IT",5)