def exchange(rub, rate):
	doll = rub / rate
	return print(f'{rub} рублей при курсе {rate} - это {doll} долларов')
	
exchange(1000, 100)
	
def adult(age):
	if age >= 18:
		adult = True
	else:
		adult = False
	return print(f'\n{adult}')

adult(18)