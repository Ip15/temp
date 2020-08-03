class Animal:
	def __init__(self, name, hunger, type, talk):
		self._name = name
		self._hunger = hunger
		self._talk = talk
		self._type = type

	def get_name(self):
		print(self._name)

	def feed(self):
		if self._hunger > 0:
			self._hunger -= 1
		print(self._hunger)

	def is_hungry(self):
		if self._hunger > 0:
			print(True)
		else:
			print(False)

	def type(self):
		self._type = type

	def talk(self):
		print(self._talk)

	def special_method(self):
		self._special_method = special_method

class Dog(Animal):
	def __init__(self, name, hunger, type = "Dog", talk = "woof woof"):
		Animal.__init__(self, name, hunger, type = "Dog", talk = "woof woof")

class Cat(Animal):
	def __init__(self, name, hunger, type = "Cat", talk = "meow"):
		Animal.__init__(self, name, hunger, type = "Cat" , talk = "meow")

def main():
	Brownie = Dog("Brownie", 10)
	Zelda = Cat ("Zelda", 3)
	zoo_lst = [Brownie, Zelda]
	for animal in zoo_lst:
		print(animal._type + " " + animal._name)
		print(animal._talk)
		while animal._hunger > 0:
			animal.feed()

main()