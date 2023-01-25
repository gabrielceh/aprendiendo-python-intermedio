# File handling

import os
import json
import csv


print("\n" + ("*~" * 10), "File handling" ,("*~" * 10))


print("\n" + ("*~" * 3), "LEER archivos archivos" ,("*~" * 3))

file = open('./my_file.txt', "r", encoding='utf-8') # abrimos el archivo
print(type(file))
# content = file.read()
# print(type(content))
# print(content)
first_line = file.readline()
print(first_line)
file.seek(0) # nos devuelve a la primera linea
all_lines = file.readlines()
print(all_lines)
file.close() # Cerramos el archivo




print("\n" + ("*~" * 3), "LEER Y ESCRIBIR archivos archivos" ,("*~" * 3))

txt = open('./my_file.txt', "a+", encoding='utf-8') # abrimos el archivo, con r+ podemos leer y escribir sin sobreescribir

txt.write("\nHe aprendido los frameworks: React js, Vue js")
txt.seek(0)
content = txt.read()
print(content)

txt.close() # Cerramos el archivo




print("\n" + ("*~" * 3), "ACTUALIZAR archivos archivos" ,("*~" * 3))

txt_2 = open("./my_file.txt","a", encoding="UTF-8")
txt_2.write("\nEsta line se hizo con a")
txt_2.close()



print("\n" + ("*~" * 3), "Abriendo archivos con with" ,("*~" * 3))

with open("./my_file.txt", "a") as f:
	f.write("\nEscribiendo con with, no necesita close")

with open("./my_file_no_exists.txt", "a+") as fil:
	fil.write("Archivo creado desde cero\n")
	print(fil.read())



print("\n" + ("*~" * 3), "Borrando Archivos" ,("*~" * 3))

if os.path.exists("./my_file_no_exists.txt"):
		os.remove("./my_file_no_exists.txt")




print("\n" + ("*~" * 3), "Trabajando con JSON" ,("*~" * 3))

# De json a dict
person_json = '''{
	"name": "Gabriel",
	"lastname": "Cervantes",
	"age": 32,
	"skills": ["Javascript","Css", "Html", "Node", "React"]
}'''

person_dict = json.loads(person_json)
print(type(person_dict))
print(person_dict)
print(person_dict["name"])

# De dict a json
country_dict = {
	"name": "Colombia",
	"capital": "Bogotá",
	"population": 51520000
}

country_json = json.dumps(country_dict, indent=4)
print(type(country_json)) # str
print(country_json)

person = {
	"name": "Gabriel",
	"lastname": "Cervantes",
	"age": 32,
	"country": "Colombia",
	"skills": ["javascript", "Css", "Html", "Node", "React"],
	"social_networks": {
		"twitter": "@gabrielcehu",
		"instagram": "@gabo_cervantes"
	}
}
with open("./person.json", "w", encoding="utf-8") as file_json:
	json.dump(person, file_json, ensure_ascii=False, indent=4)

with open("./person.json", "r+", encoding="utf-8") as file_json:
	for line in file_json:
		print(line)
	
	file_json.seek(0)
	
	my_json = json.load(file_json)
	print(my_json)
	print(my_json["social_networks"]["instagram"])




print("\n" + ("*~" * 3), "Trabajando con CSV" ,("*~" * 3))

with open('./person_list.csv', newline='') as csv_file:
	reader_csv = csv.reader(csv_file, delimiter=' ', quotechar="|")
	print(reader_csv)

	for index,row in enumerate(reader_csv):
		if index == 0:
			print(f"Columnas: {row[0]} {row[1]} {row[2]}")
		else:
			print(f"{row[0]} - {row[1]} - {row[2]}")

with open('./person_list.csv', 'a', newline='') as csvfile:
	writer_csv = csv.writer(csvfile, delimiter=" ", quotechar="|")
	writer_csv.writerow(["Apsu", "Cervantes Hurtado",7])