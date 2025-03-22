class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        if self.species == "Dog":
            return "Woof!"
        elif self.species == "Cat":
            return "Meow!"
        elif self.species == "Bird":
            return "Chirp!"
        else:
            return "Unknown sound."

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                return
        print(f"Animal with name {name} not found.")

    def list_animals(self):
        for animal in self.animals:
            print(f"Animal: {animal.name}, Species: {animal.species}, Age: {animal.age}")

    def make_all_speak(self):
        for animal in self.animals:
            print(f"{animal.name} says: {animal.speak()}")

# 測試程式
animal1 = Animal("Leo", "Dog", 3)
animal2 = Animal("Mimi", "Cat", 2)
animal3 = Animal("Tweety", "Bird", 1)

zoo = Zoo()
zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_animal(animal3)

print("Initial animal list:")
zoo.list_animals()

print("\nAll animals speak:")
zoo.make_all_speak()

zoo.remove_animal("Mimi")

print("\nAfter removing Mimi:")
zoo.list_animals()