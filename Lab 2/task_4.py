# class

class f_c:
    name = "Haris"
    dep = "IT"
    sem = 5

x = f_c()
print(x.name)
print(x.dep)
print(x.sem)

# class init
class intro:
    def __init__(self, name, dep, sem):
        self.name=name
        self.dep=dep
        self.sem=sem

    def intro_fun(self):
        print("Name: "+""+self.name)
        print("Department: "+""+self.dep)
        print("Semester: "+""+str(self.sem))
p1 = intro("Haris","IT",5)
print(p1.name)
print(p1.dep)
print(p1.sem)

p1.intro_fun()