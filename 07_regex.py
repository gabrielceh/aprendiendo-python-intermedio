# Regular Expression

import re

print("\n" + ("*~" * 10), "REGEX" ,("*~" * 10))
my_string = "Esta es la clase 7: Expresiones Regulares"
my_other_string = "Esta no es la clase 6: manejo de ficheros"

print(f"my_string: {my_string}")
print(f"my_other_string: {my_other_string}")

print("\n" + ("*~" * 3), "match" ,("*~" * 3))
patron_macth = "Esta es la clase 7"
match_1 = re.match(patron_macth, my_string, re.I)
match_2 = re.match(patron_macth, my_other_string, re.I)

print(f"re.match('Esta es la clase 7', my_string, re.I): {match_1}")
print(f"match_1.span(): posicion {match_1.span()}")
print(f"match_1.start(): posicion inicial{match_1.start()}")
print(f"match_1.end(): posicion final {match_1.end()}")
print(f"my_string[match_1.start():match_1.end()]: {my_string[match_1.start():match_1.end()]}")
print(f"match_1.group(): {match_1.group()}")
print(f"re.match('Expresiones Regulares', my_string, re.I): {re.match('Expresiones Regulares', my_string, re.I)}")
print(f"re.match('Esta es la clase 7', my_other_string, re.I): {re.match('Esta es la clase 7', my_other_string, re.I)}")

if match_1 != None:
	start, end = match_1.span()
	print(f"Si paso la validacion: {my_string[start:end]}")
else:
	print(f"No hizo match: cadena = {my_string}- patron: 'Esta es la clase 7'")

if match_2 != None:
	start, end = match_2.span()
	print(f"Si paso la validacion: {my_other_string[start:end]}")
else:
	print(f"No hizo match: cadena = {my_other_string}- patron: 'Esta es la clase 7'")


print("\n" + ("*~" * 3), "search" ,("*~" * 3))

patron_search = "clase 7"
search_1 = re.search(patron_search, my_string, re.I)
search_2 = re.search(patron_search, my_other_string, re.I)

print(f"re.search(patron_search, my_string, re.I) : {search_1}")
print(f"search_1.span() : posicion {search_1.span()}")
print(f"re.search(patron_search, my_other_string, re.I) : {search_2}")

if search_1 is not None:
	start, end = search_1.span()
	print(f"Si pasó la validacion: {my_string[start:end]}")
else:
	print(f"No pasó: cadena = {my_string}- patron: '{patron_search}'")


if search_2 is not None:
	start, end = search_1.span()
	print(f"Si pasó la validacion: {my_other_string[start:end]}")
else:
	print(f"No pasó: cadena = {my_other_string}- patron: '{patron_search}'")


print("\n" + ("*~" * 3), "findall" ,("*~" * 3))

my_new_string = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
my_new_string_2 = '''Me encanta javascript, pero ahora estoy aprendiendo python'''

print(f"my_new_string: {my_new_string}")
patter_findall = "language"

findall_1 = re.findall(patter_findall, my_new_string, re.I)
findall_2 = re.findall(patter_findall, my_new_string_2, re.I)

print(f"re.findall(patter_findall, my_new_string, re.I): {findall_1}")
print(f"re.findall(patter_findall, my_new_string_2, re.I): {findall_2}")




print("\n" + ("*~" * 3), "split" ,("*~" * 3))

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))



print("\n" + ("*~" * 3), "sub" ,("*~" * 3))

to_replace = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

new_to_replace = re.sub("[Pp]ython","Javascript",to_replace)

print(f"original: {to_replace}")
print(f"new: {new_to_replace}")



print("\n" + ("*~" * 3), "Patrones de expresiones regulares" ,("*~" * 3))

my_string = "Esta es la lección 7: Expresiones Regulares"

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))

name = "Gabriel Cervantes Hurtado"
print(re.match(r'^[A-Z|a-z| ]+$', email))
print(re.match(r'^[A-Z|a-z| ]+$', name))