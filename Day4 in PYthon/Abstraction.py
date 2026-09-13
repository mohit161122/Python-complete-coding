from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")


lion = Lion()
lion.make_sound()