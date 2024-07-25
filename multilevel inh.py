class Animal:
    def speak():
        return "Animal is speaking"
# Single inheritance:
class Dog(Animal):
    def Bark():
        return "Bow..."
class Puppy(Dog):
    def puppy_speak():
        return "Iam puppy"

obj1=Animal
obj2=Dog
obj3=Puppy
print(obj1.speak())
print(obj2.speak())
print(obj2.Bark())
print(obj3.speak())
print(obj3.Bark())
print(obj3.puppy_speak())