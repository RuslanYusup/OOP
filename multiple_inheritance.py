# один потомок от множественного родителя

class parent1:
	def __init__(self):
		 super().__init__()
		 self.smart = "smart"
		 self.hair_colour = "light"

class parent2:
	def __init__(self):
		 super().__init__()
		 self.pretty = "pretty"
		 self.hair_colour = "dark"

class Child(parent1, parent2):
	def __init__(self):
		 super().__init__()
	
	def traits(self):
		print(self.pretty)
		print(self.smart)
		print(self.hair_colour)

child = Child()
child.traits()

# порядок разрешения методов, первый родитель parent1, поэтому идем за атрибутом к нему
