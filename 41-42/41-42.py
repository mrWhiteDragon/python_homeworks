class Car:
	def __init__(self, color, fuel, consumption, mileage=0
	):
		self.color = color
		self.fuel = fuel
		self.consumption = consumption
		self.mileage = mileage
		print(f'Создали машину. Цвет: {self.color}, топливо: {self.fuel}л')
		
	def drive(self, km):
		need_fuel = self.consumption / 100 * km
		if need_fuel <= self.fuel:
			print(f'Мы проехали {km} км')
			self.fuel -= need_fuel
			print(f'Осталось топлива: {round(self.fuel)}л')
			self.mileage += km
		else:
			print(f'Не хватит топлива')
	
	def get_mileage(self):
		return print(f'Пробег: {self.mileage}км')

car_1 = Car(color="красный", fuel=10, consumption=10 )
car_1.drive(80)
car_1.get_mileage()
	