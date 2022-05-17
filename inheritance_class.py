
# Построим иерархию наследования классов по машинам


class Vehicle:
	def __init__(self, maker, model, colour, price, seats):
		self.maker = maker
		self.model = model
		self.colour = colour
		self.price = price


class Car(Vehicle):
	def __init__(self, maker, model, colour, price, seats):
		super().__init___(maker, model, colour, price) # все, что наследуем
		self.seats = seats

class Industrial_Vehicle(Vehicle):
	def __init__(self, maker, model, colour, price, lifting_weight):
		super().__init___(maker, model, colour, price)
		self.lifting_weight = lifting_weight


class Forklift(Industrial_Vehicle):
	def __init__(self, maker, model, colour, price, lifting_weight):
		super().__init___(maker, model, colour, price, lifting_weight)

class Crane:
	def __init__(self, maker, model, colour, price, lifting_weight):
		super().__init___(maker, model, colour, price, lifting_weight)



car_1 = Car("Opel", "Mokka", "Black", 2000)
forklift = Forklift("Honda", "fl1", "Brown", 15000, 5)
crane = Crane("Canterpillar", "cr1", "Yellow", 65000, 15)

print(car_1.maker, car_1.model, car_1.colour, car_1.price, car_1.seats)