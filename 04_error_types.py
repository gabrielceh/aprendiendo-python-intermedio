# Error types

print("\n" + ("*~" * 10), "Error Types" ,("*~" * 10))

print("\n" + ("*~" * 3), "SyntaxError" ,("*~" * 3))

try:
	# print "Hola mundo" # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
	pass
except SyntaxError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "NameError" ,("*~" * 3))

try:
	total = num_1+ 2 # NameError: name 'num_1' is not defined
	print(total)
except NameError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "IndexError" ,("*~" * 3))
try:
	my_list = ["🥞","🍪","🥐","🌮","🍝","🌭","🍫"]
	print(my_list[2])
	print(my_list[11]) # list index out of range
except IndexError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "ModuleNotFoundError" ,("*~" * 3))

try:
	import maths # No module named 'maths'
except ModuleNotFoundError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "AttributeError" ,("*~" * 3))
try:
	my_num = 19
	my_num.append(10) # 'int' object has no attribute 'append'
	print(my_num)
except AttributeError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "KeyError" ,("*~" * 3))

try:
	person = {
		"name": "Gabriel",
		"age" : 32,
		"country": "Colombia",
		"is_single": False,
		"social_networks": {
			"twitter": "https://twitter.com/gabrielcehu",
			"instagram": "https://www.instagram.com/gabo_cervantes/",
			"twitch":"https://www.twitch.tv/gaelbq27"
		}
	}

	print(person["name"])
	print(person["social_networks"])
	print(person["edad"]) # edad
except Exception as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "TypeError" ,("*~" * 3))

try:
	total = 1 + "2" # unsupported operand type(s) for +: 'int' and 'str'
	print(total)
except TypeError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "ImportError" ,("*~" * 3))
try:
	from math import PI # cannot import name 'PI' from 'math' (unknown location)
	from math import pi # correcto

	print(PI)

except ImportError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "ValueError" ,("*~" * 3))
try:
	num = int("Hola") # invalid literal for int() with base 10: 'Hola'
	print(num)
except ValueError as err:
	print(f"Error: {err}")



print("\n" + ("*~" * 3), "ZeroDivisionError" ,("*~" * 3))
try:
	div = 4 / 0 # division by zero
	print(div)
except ZeroDivisionError as err:
	print(f"Error: {err}")