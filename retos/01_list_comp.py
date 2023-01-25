"""
1. Filter only negative and zero in the list using list comprehension
	numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""
print("\n" + ("*~" * 10), "Ejercicio 1" ,("*~" * 10))

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_neg_and_zero = [i for i in numbers if i <= 0]
print(f"Only negative and zero: {only_neg_and_zero}")


"""
2.Flatten the following list of lists of lists to a one dimensional list :
	list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]	
	output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
print("\n" + ("*~" * 10), "Ejercicio 2" ,("*~" * 10))

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [number for row in list_of_lists for list in row for number in list]
print(f"Flated list: {flat_list}")


"""
3. Using list comprehension create the following list of tuples:
	[(0, 1, 0, 0, 0, 0, 0),
	(1, 1, 1, 1, 1, 1, 1),
	(2, 1, 2, 4, 8, 16, 32),
	(3, 1, 3, 9, 27, 81, 243),
	(4, 1, 4, 16, 64, 256, 1024),
	(5, 1, 5, 25, 125, 625, 3125),
	(6, 1, 6, 36, 216, 1296, 7776),
	(7, 1, 7, 49, 343, 2401, 16807),
	(8, 1, 8, 64, 512, 4096, 32768),
	(9, 1, 9, 81, 729, 6561, 59049),
	(10, 1, 10, 100, 1000, 10000, 100000)]
"""
print("\n" + ("*~" * 10), "Ejercicio 3" ,("*~" * 10))

def pow_to_tuple(num, range_pow:int):
	my_list = [num ** i for i in range(range_pow)]
	my_list.insert(0, num)
	my_tuple = tuple(my_list)
	
	return my_tuple


list_pow = [pow_to_tuple(i,6) for i in range(11)]
print(f"List pow: {list_pow}")


"""
4. Flatten the following list to a new list:
	countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
	output:
	[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""
print("\n" + ("*~" * 10), "Ejercicio 4" ,("*~" * 10))

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def slice_country(country:list):
	original = country[0]
	capital = country[1]
	code = country[0][0:3].upper()
	
	return [original, code, capital]

flat_countries = [slice_country(country) for row in countries for country in row]

print(f"flat contries: {flat_countries}")


"""
5. Change the following list to a list of dictionaries:
	countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
	output:
	[{'country': 'FINLAND', 'city': 'HELSINKI'},
	{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
	{'country': 'NORWAY', 'city': 'OSLO'}]
"""
print("\n" + ("*~" * 10), "Ejercicio 5" ,("*~" * 10))

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_dicc = [{"country":country[0].upper(), "city":country[1].upper()} for row in countries for country in row]

print(f"countries dicc: {countries_dicc}")
