# Lambdas

print("\n" + ("*~" * 10), "Lambdas" ,("*~" * 10))

sum_two_values = lambda num_one, num_two : num_one + num_two
print(f"lmabda sum_two_values(1,4): {sum_two_values(1,4)}")

is_even = lambda n: n % 2 == 0
print(f"is_even(4): {is_even(4)}")
print(f"is_even(5): {is_even(5)}")



print("\n" + ("*~" * 10), "Self invoking" ,("*~" * 10))
print((lambda num_1, num_2: num_1 * num_2)(2,3))



print("\n" + ("*~" * 10), "Lambdas dentro de funciones" ,("*~" * 10))

def power(x):
	return lambda n: x ** n

cube = power(2)(3)
print(f"cube(2)(3): {cube}") # x -> 2, n -> 3
