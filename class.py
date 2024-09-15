class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Your name is {self.name}. You are {self.age}, and your gender is {self.gender}"

person1 = Person('Tshidi', 20, 'male')
print(person1)