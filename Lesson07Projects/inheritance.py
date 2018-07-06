class Parent():
    def __init__(self, lastName, eyeColour):
        print("Parent Constructor called")
        self.lastName = lastName
        self.eyeColour = eyeColour

    def showInfo(self):
        print("last name: " + self.lastName)
        print("eyes colour: " + self.eyeColour)


class Child(Parent):
    def __init__(self, lastName, eyeColour, numberOfToys):
        print("Child Constructor called")
        Parent.__init__(self, lastName, eyeColour)
        self.numberOfToys = numberOfToys

    def showInfo(self):
        super().showInfo()
        print("number of toys: " + str(self.numberOfToys))


billyCyrus = Parent("Cyrus", "Blue")
# billyCyrus.showInfo()
# print(billyCyrus.lastName)

mileyCyrus = Child("Cyrus", "Blue", 5)
mileyCyrus.showInfo()
# print(mileyCyrus.lastName)
# print(mileyCyrus.numberOfToys)