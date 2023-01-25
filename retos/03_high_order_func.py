countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n" + ("*~" * 10), "Originals" ,("*~" * 10))
print(countries)
print(names)
print(numbers)

from functools import reduce
from countries import countries as all_countries

"""
1. Use map to create a new list by changing each country to uppercase in the countries list
"""
print("\n" + ("*~" * 10), "Ejercicio 1" ,("*~" * 10))

countries_upper = list(map(lambda country: country.upper(), countries))
print(f"countries upper: {countries_upper}")

"""
2. Use map to create a new list by changing each number to its square in the numbers list
"""
print("\n" + ("*~" * 10), "Ejercicio 2" ,("*~" * 10))

numbers_square = list(map(lambda number: number ** 2, numbers))
print(f"numbers square: {numbers_square}")

"""
3. Use map to change each name to uppercase in the names list
"""
print("\n" + ("*~" * 10), "Ejercicio 3" ,("*~" * 10))

names_uppercase = list(map(lambda name: name.upper(), names))
print(f"names upper: {names_uppercase}")

"""
4. Use filter to filter out countries containing 'land'.
"""
print("\n" + ("*~" * 10), "Ejercicio 4" ,("*~" * 10))

countries_land = list(filter(lambda country: 'land' in country.lower(), countries))
print(f"no land: {countries_land}")

"""
5. Use filter to filter out countries having exactly six characters.
"""
print("\n" + ("*~" * 10), "Ejercicio 5" ,("*~" * 10))

exact_6_char = list(filter(lambda country: len(country) == 6, countries))
print(f"no 6 characters: {exact_6_char}")

"""
6. Use filter to filter out countries containing six letters and more in the country list.
"""
print("\n" + ("*~" * 10), "Ejercicio 6" ,("*~" * 10))

more_6_char = list(filter(lambda country: len(country) > 6, countries))
print(f"less 6 characters: {more_6_char}")

"""
7. Use filter to filter out countries starting with an 'E'
"""
print("\n" + ("*~" * 10), "Ejercicio 7" ,("*~" * 10))

start_with_E = list(filter(lambda country: country.startswith('E'), countries))
print(f"start with 'E': {start_with_E}")

"""
8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
"""
print("\n" + ("*~" * 10), "Ejercicio 8" ,("*~" * 10))

chain = (reduce(lambda acc, x: acc + x, filter(lambda x: x % 2 == 0, map(lambda x: x ** 3, numbers)))) # se le de atras para adelante
print(chain)

"""
9.Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
"""
print("\n" + ("*~" * 10), "Ejercicio 9" ,("*~" * 10))

def get_string_list(items_list):
	copy_list = list(filter(lambda item: type(item) == str, items_list))

	return copy_list

my_items = [1, False, "🌭", "🍓", 1.86, {"saludo":"hola"}]
print(get_string_list(my_items))

"""
10. Use reduce to sum all the numbers in the numbers list.
"""
print("\n" + ("*~" * 10), "Ejercicio 10" ,("*~" * 10))

sum_total = reduce(lambda acc, num: acc + num, numbers)

print(f"sum_total: {sum_total}")


"""
11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
"""
print("\n" + ("*~" * 10), "Ejercicio 11" ,("*~" * 10))

def conct_string(acc, item):
	print(f'item:{item} -  acc: {acc}')
	if acc == "Estonia":
		acc += ", " + item + ", "
	elif item != 'Iceland' and item != 'Norway':
		acc += item + ", "
	elif item == 'Norway':
		acc += 'Norway and '
	else:
		acc += "Iceland are north Eurpean countries"
	return acc

def concatenate_countries(countries_list):
	conct_countries = reduce(conct_string, countries_list)
	print(conct_countries)
	return (f"")

print(concatenate_countries(countries))


"""
12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
"""
print("\n" + ("*~" * 10), "Ejercicio 12" ,("*~" * 10))

def categorize_countries(pattern, list_item):
	filter_countries = list(filter(lambda item: pattern in item, list_item))
	return filter_countries



print(f"ia countries: {categorize_countries('ia', all_countries)}")
print(f"land countries: {categorize_countries('land', all_countries)}")

"""
13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
"""
print("\n" + ("*~" * 10), "Ejercicio 13" ,("*~" * 10))

def country_dict(countries:list):
	letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	my_dic = {}
	
	for letter in letters:
		countries_list = list(filter(lambda x: x.upper().startswith(letter),countries))
		countries_len = len(countries_list)
		my_dic[letter] = countries_len
	
	return my_dic

print(country_dict(all_countries))


"""
14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
"""
print("\n" + ("*~" * 10), "Ejercicio 14" ,("*~" * 10))

def get_first_ten_countries(countries:list):
	my_ten_first_items = []
	for (i, item) in enumerate(countries):
		if i >= 10:
			break
		my_ten_first_items.append(item)
	return my_ten_first_items


print(get_first_ten_countries(all_countries))

"""
15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
"""
print("\n" + ("*~" * 10), "Ejercicio 15" ,("*~" * 10))

def get_last_ten_countries(countries:list):
	my_ten_last_items = []
	countries_copy = countries.copy()
	countries_copy.reverse()
	for (i, item) in enumerate(countries_copy):
		if i >= 10:
			break
		my_ten_last_items.append(item)

	my_ten_last_items.reverse()

	return my_ten_last_items

print(get_last_ten_countries(all_countries))