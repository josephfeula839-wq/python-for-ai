class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __init__(self, source):
        self.name = source.name
        self.age = age

jose = Dog("Jose", 5)
print(jose.name)  # Output: Jose
print(jose.age)   # Outpu

vaza = Dog(jose)
##test comment
print(vaza.name)  # Output: Jose
print(vaza.age)   # Output: 5