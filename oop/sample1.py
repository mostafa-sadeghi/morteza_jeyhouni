class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name}, Good Boy EatUp")
        else:
            print(f"{self.name}, Good Girl EatUp")

    def bark(self):
        print("WOOF WOOF WOOF")


class Beagle(Dog):
    def __init__(self, name, age, gender, gunshy):
        super().__init__(name, age, gender)
        self.gunshy = gunshy

    def hunt(self):
        print(f"{self.name} is hunting so good")


beagle_1 = Beagle("jessi", 2, "girl", True)
beagle_1.bark()
beagle_1.hunt()
