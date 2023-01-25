def suma():
	r"""
		Suma los numeros enteros o flotantes que le pasemos
	"""
	def add(*args:int):
		total = 0
		for num in args:
			total += num
		return total
	
	return add