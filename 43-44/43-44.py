#1)
import random

class Car:
	def __init__(self, color, fuel, consumption, mileage=0
	):
		self.color = color
		self.fuel = fuel
		self.consumption = consumption
		self.mileage = mileage
		print(f'\nСоздали машину. Цвет: {self.color}, топливо: {self.fuel}л')
		
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
		
class SportCar(Car):
	def fast_drive(self, km):
		need_fuel = self.consumption * 1.5 / 100 * km
		if need_fuel <= self.fuel:
			print(f'Мы проехали {km} км')
			self.fuel -= need_fuel
			print(f'Осталось топлива: {round(self.fuel)}л')
			self.mileage += km
		else:
			print(f'Не хватит топлива')
			
	def competition(self):
		victory = random.choice([True, False])
		if victory:
			print('Машина выиграла в соревнованиях')
		else:
			print('Машина проиграла в соревнованиях')

car_1 = Car(color="красный", fuel=10, consumption=10 )
car_1.drive(80)
car_1.get_mileage()

car_2 = SportCar(color="желтый", fuel=12, consumption=10)
car_2.fast_drive(50)
car_2.get_mileage()
car_2.competition()

#2)
class Programmer:
	SALARY_INFO = {'Junior': 10, 'Middle': 15, 'Senior': 20}
	
	def __init__(self, name, position):
		self.name = name
		self.position = position
		self.all_time = 0
		self.all_salary = 0
		
		self.salary = self.SALARY_INFO[self.position]
		print(f'\nНовый программист. Имя: {self.name}, должность: {self.position}')
		
	def work(self, time):
		self.all_time += time
		salary = self.salary * time
		self.all_salary += salary
		print(f'Отработал {time}ч.')
			
	
	def rise(self):
		if self.position == 'Junior':
			self.position = 'Middle'
			self.salary = self.SALARY_INFO[self.position]
			
		elif self.position == 'Middle':
			self.position = 'Senior'
			self.salary = self.SALARY_INFO[self.position]
			
		elif self.position == 'Senior':
			self.salary += 1
			
		print(f'Повышение. Должность: {self.position}')
			
	def info(self):
		print(f'{self.name} {self.all_time}ч. {self.all_salary}тгр.')
		
programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
programmer.info()
programmer.rise()
programmer.work(500)
programmer.info()
programmer.rise()
programmer.work(250)
programmer.info()
programmer.rise()
programmer.work(250)
programmer.info()

