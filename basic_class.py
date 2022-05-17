

# описание машины и способы взаимодействей с ней (покупка и пр)

class Car:
	PURCHASE_TYPE = ("LEASE", "CASH")  #глобальные переменные

	__sales_list = None


	@staticmethod #статический метод
	def get_sales_list():
		if Car.__sales_list == None:
			Car.__sales_list = []
		return Car.__sales_list


	@classmethod
	def get_purchase_types(cls):
		return cls.PURCHASE_TYPE
	
	def __init__(self, maker, model, color, price, purchase_type):
		self.maker = maker
		self.model = model
		self.color = color
		self.price = price
		self.__secret_cog = "TSHH" # позволяет избежать переписывание
		if (not purchase_type in Car.PURCHASE_TYPE):
			raise ValueError(f"{purchase_type} это не то, шел бы ты со своей валюткой")
		else:
			self.purchase_type = purchase_type

	def get_price(self):
		if hasattr(self, "_discount"):
		 		return self.price - (self.price * self._discount) #проверяет существует ли отдельный атрибут в классе
		else:
			return self.price
	
	def set_discount(self, amount):
		self._discount = amount #внутриклассовый, условно защищенный
	

class Boat:
	def __init__(self, name):
		self.name = name


car1 = Car("BMW", "i8", "white", 50000, "CASH")
car2 = Car("Mersedes", "C-class", "black", 28500, "SWAP")

print("Валюта:", Car.get_purchase_types())

print(car2.purchase_type)

sales_this_month = Car.get_sales_list()
sales_this_month.append(car1)
sales_this_month.append(car2)

print(sales_this_month)







# isinstance = проверка классов в рамках ветвления
# статические методы не меняют состояние класса или экземпляра, 
# например создадим список, который занимается отслеживанием продаж и скроем его за пределы класса
