class Shop:
	PRODUCTS = {'колбаса': 20, 'молоко': 10}
	DISCOUNT = ['молоко']
	def __init__(self):
		self.count = 0
		self.all_sum = 0
	
	def buy(self, name):
		name = name.lower()
		if name in self.PRODUCTS:
			price = self.PRODUCTS[name]
			if self._check_discount(name):
				price -= 5
			self.count += 1
			self.all_sum += price
			print(f'Купили {name}')
		else:
			print('Такого товара нет')
			
	def add_product(self, name, price):
		name = name.lower()
		self.PRODUCTS[name] = price
		print('Продукт добавлен')
		
	def delete_product(self, name):
		name = name.lower()
		if name in self.PRODUCTS:
			self.PRODUCTS.pop(name)
			print(f'Удалили {name}')
		else:
			print('Такого товара нет')
			
	def get_info(self):
			print(f'Всего куплено товаров на сумму {self.all_sum}р.')
			print(f'Всего чеков {self.count}')
			print('Хорошего дня!')
			
	def _check_discount(self, name):
			return name in self.DISCOUNT
			
shop = Shop()
shop.buy('Молоко')
shop.buy('Яйца')
shop.buy('Колбаса')
shop.add_product('Яйца', 100)
shop.buy('Яйца')
shop.delete_product('Молоко')
shop.buy('Молоко')
shop.get_info()

		