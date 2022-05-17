# предотращение инициации родительского класса
# ABC - библиотека абстрактного метода
# интерфейсы - чертеж для разработки классов



from abc import ABC, abstractclassmethod


class Shipping(ABC):
	@abstractclassmethod
	def shipping(self, transport):
		pass

class Electrical_Appliance (ABC):
	def __init__(self):
		 super().__init__()
	
	@abstractclassmethod #отнаследовал от абстрактного класса, т.е. в родительском методе ничего не делает
	def electricity_consumption(self):
		pass


class Heater(Electrical_Appliance, Shipping):
	def __init__(self, heating):
		 self.heating = heating

	def electricity_consumption(self): #переопределили методы
		return 1500 * self.heating

	def shipping(self, transport):
		 self.transport = transport
		 return transport

class Cooler(Electrical_Appliance):
	def __init__(self, cooling):
		self.cooling = cooling
	def electricity_consumption(self): 
		return 1200 * self.cooling

#e = Electrical_Appliance() иначе ошибка - попытка создать экземляр абстрактного класса

h = Heater(50)
print(h.heating, h.electricity_consumption(), h.shipping("Cargo"))

c = Cooler(20)
print(c.cooling, c.electricity_consumption())