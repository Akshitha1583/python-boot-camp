class Father:
    def father_speak():
        return "Father class"
class Mother:
    def mother_speak():
        return "Mother class"
class Kid(Father,Mother):
    def kid_speak():
        return "Iam kid having properties of Mother and Father"
obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())
