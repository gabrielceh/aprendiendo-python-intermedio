# Decorators

print("\n" + ("*~" * 10), "Decorators" ,("*~" * 10))

def uppercase_decorator(function):
	def wrapper():
		func = function()
		print('* Se ha llamado a upper')
		to_upper = func.upper()
		return to_upper
	return wrapper



@uppercase_decorator
def gretting():
	return "hello"

print(gretting())

print("\n" + ("*~" * 10), "Decorators multiples" ,("*~" * 10))

def split_str_decorator(function):
	def wrapper():
		func = function()
		print('* Se ha llamado a split')
		split_str = func.split()
		return split_str
	return wrapper

# se ejecuta primero el de mas abajo
@split_str_decorator
@uppercase_decorator
def saludo():
	saludo = "Hola python"
	print("* ejecucion de la funcion")
	return saludo

print(saludo())


print("\n" + ("*~" * 10), "Decorators con paramtros en la funcion" ,("*~" * 10))

def to_title_decorator(function):
	def wrapper(string):
		func = function(string)
		to_title = func.title()
		return to_title
	return wrapper


@to_title_decorator
def saludo_2(saludo):
	return saludo


print(saludo_2('Hola mundo, estoy muy feliz hoy'))
		



