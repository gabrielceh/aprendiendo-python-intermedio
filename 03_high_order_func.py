# High Oder Functions
from functools import reduce

print("\n" + ("*~" * 10), "High order function" ,("*~" * 10))

def sum_one(value):
	return value + 1

def sum_five(value):
	return value + 5



def sum_two_values_and_one(first_val, second_val, f_sum):
	return sum_one(first_val + second_val)

def sum_two_values_and_value(first_val, second_val, f_sum):
	return f_sum(first_val + second_val)

print(sum_two_values_and_value(1,2, sum_one))
print(sum_two_values_and_value(1,2, sum_five))


print("\n" + ("*~" * 10), "Closures" ,("*~" * 10))

def sum_ten():
	ten = 10
	def add(num):
		return num + ten
	return add

result = sum_ten()

print(f"result(10): {result(10)}")
print(f"result(5): {result(5)}")
print(f"sum_ten()(3): {sum_ten()(3)}")


print("\n" + ("*~" * 10), "High order function del lenguaje" ,("*~" * 10))
print("\n" + ("*~" * 3), "Map" ,("*~" * 3))

numbers = list(range(51))

def square(x):
	return x ** 2

numbers_squared = (map(square, numbers))
print(list(numbers_squared))

numbers_squared_two = map(lambda x: x ** 2, numbers)
print(list(numbers_squared_two))


print("\n" + ("*~" * 3), "Filter" ,("*~" * 3))

def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

even_numbers_two = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers_two))


print("\n" + ("*~" * 3), "Reduce" ,("*~" * 3))
print("from functools import reduce")

def add_two_numbers(x, y):
	print(f"x -> {x} ... y -> {y}")
	return int(x) + int(y)

total = reduce(add_two_numbers, numbers)
print(total)
