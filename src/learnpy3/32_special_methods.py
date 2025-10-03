# Special Methods & Attributes

class Snowflake:
    pass

flake = Snowflake()

print(dir(flake))

class Martian:
    pass

m1 = Martian()
print(m1.__dict__)
m1.first_name = 'Owen'
m1.last_name = 'Phelps'
print(m1.__dict__)

class Martini:
    """Someone who lives on Martini."""

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        # print(f">>> You set {name} = {value}")
        self.__dict__[name] = value

    def __getattr__(self, name):
        print(f">>> Get the {name} attribute")
        if name == 'full_name':
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"No attribute named {name}")
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __lt__(self, other):
        print(f">>> Comparing {self} with {other}")
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)



print(Martini.__doc__)
m2 = Martini("Gregor", "Sajovic")
m2.arrival_date = '2023-02-03'
print(m2.__dict__)


m = Martini('Pierre', 'Aberg')
print(f"First name = {m.first_name}")
print(f"Last name = {m.last_name}")
print(m.full_name)
# print(m.martian_name)
print(m.__dict__)

# Note that if the attribute is found through the normal mechanism, 'get attribute' is not called.
# (This is an intetntional asymmetry between 'get attribute' and 'set attribute'.)
# This is done both for efficiency reasons and because otherwise 'get attribute' would have no way to access other attributes of the instance.

m3 = Martini("Joško", "Buha")
print(m3)
print(m3.__str__())
print(id(m3))


m4 = Martini("Rod", "Stewart")
print(m4)

# Compare Martinis
# Order by name: martini1 < martini2

mA = Martini("Cyrille", "Collins")
mB = Martini("Len", "Klein")
mC = Martini("Matthias", "Stein")
mD = Martini("Mike", "Lenox")
mE = Martini("Bob", "Hillier")
mF = Martini("Olwyn", "Meek")
mG = Martini("Andy", "Taylor")
mH = Martini("Halbert", "Stone")
mI = Martini("Marvin", "Meek")

martians = [mA, mB, mC, mD, mE, mF, mG, mH, mI]
martians.sort()
for m in martians:
    print(m)

