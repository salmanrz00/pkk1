class person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("My name is ", self.name)

person1 = person("Salman")
person1.say_hi()