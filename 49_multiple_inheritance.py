# multiple inheritance = inherit from more than one parent class C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")


class Pray(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")


class Rabbit(Pray):
    pass


class Hawk(Predator):
    pass


class Fish(Pray, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

hawk.sleep()
