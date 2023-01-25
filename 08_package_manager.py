# Python Package manager

print("\n" + ("*~" * 10), "Python Package Manager" ,("*~" * 10))

# PIP https://pypi.org

# pip install pip
# pip --version

import numpy # pip install numpy
import requests # pip install requests
import json
from my_package import aritmetica # creado

print("\n" + ("*~" * 3), "pip install numpy" ,("*~" * 3))
print(f"numpy version: {numpy.version.version}")

numpy_array = numpy.array([1,2,3,4,5,6,7,8,9,10])

print(f"type(numpy_array): {type(numpy_array)}")

print(f"numpy_array: {numpy_array}")
print(f"numpy_array * 2: {numpy_array * 2}")

print("\n" + ("*~" * 3), "pip install requests" ,("*~" * 3))
#https://pypi.org/project/requests/

user_pokemon = input('Ingresa el nombre de un pokémon: ')
try:
	response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_pokemon}")

	print(response)
	print(f"response.status_code: {response.status_code}")
	# print(f"response.headers: {response.headers}")
	# print(f"response.json(): {response.json()}")

	if response.status_code >= 200 and response.status_code < 300:
		pokemon = response.json()
		print(f"pokemon['name]: {pokemon['name']}")
		pokemon_name = pokemon["name"]

		with open(f"./pokemon/{pokemon_name}.json", "w", encoding="UTF-8") as file:
			json.dump(pokemon, file, ensure_ascii=False, indent=4)
			print('File saved succesfully')
	else:
		print(f"pokemon '{user_pokemon}' not found")

except Exception as exc:
	print(exc)


print("\n" + ("*~" * 3), "Paquete propio" ,("*~" * 3))

suma = aritmetica.suma()

print(suma(1,4))
print(suma(142,454,23))
print(suma(453,3245,1,98))