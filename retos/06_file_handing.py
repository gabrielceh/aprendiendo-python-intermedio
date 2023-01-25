import re
import json

path_file = "./retos/data/"
countries_path = path_file + "countries_data.json"

"""
1.	Write a function which count number of lines and number of words in a text. 
	All the files are in the data the folder: 
		a) Read obama_speech.txt file and count number of lines and words 
		b) Read michelle_obama_speech.txt file and count number of lines and words 
		c) Read donald_speech.txt file and count number of lines and words 
		d) Read melina_trump_speech.txt file and count number of lines and words
"""


print("\n" + ("*~" * 10), "Ejercicio 1" ,("*~" * 10))

def count_words_and_lines(file_path:str):
	with open(file_path, "r", newline="", encoding="utf-8") as f:
		f.seek(0)
		lines = f.readlines()
		count_words = 0

		for line in lines:
			if len(line) > 1:
				word_list = line.split(' ')
				for item in word_list:
					if re.search("[\w]",item):
						count_words = count_words + 1
	
	return {"words": count_words, "lines": len(lines)}	


print(f"Barack Obama Speech: {count_words_and_lines(path_file + 'barack_obama_speech.txt')}")
print(f"Michelle Obama Speech: {count_words_and_lines(path_file + 'michelle_obama_speech.txt')}")
print(f"Melina Trump Speech: {count_words_and_lines(path_file + 'melina_trump_speech.txt')}")
print(f"Donald Trump Speech: {count_words_and_lines(path_file + 'donald_trump_speech.txt')}")


"""
2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
"""
print("\n" + ("*~" * 10), "Ejercicio 2" ,("*~" * 10))

def most_spoken_languages(file_name:str, quantity:int):
	countries_list = []
	with open(file_name, "r", encoding="utf-8") as file:
		countries_list = json.load(file)

	languages_list = []
	for country in countries_list:
		for language in country["languages"]:
			languages_list.append(language)

	languages_sorted_list = sorted(languages_list)
	languages_spoken_list = []

	for (index,language) in enumerate(languages_sorted_list):
		if(index == 0):
			languages_spoken_list.append((languages_list.count(language), language))
		elif language != languages_sorted_list[index - 1]:
			languages_spoken_list.append((languages_list.count(language), language))
		else:
			continue

	languages_spoken_sorted_list = sorted(languages_spoken_list, key=lambda item: item[0], reverse=True)


	return languages_spoken_sorted_list[0:quantity]


print(most_spoken_languages(countries_path, 3))



"""
3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
"""
print("\n" + ("*~" * 10), "Ejercicio 3" ,("*~" * 10))

def most_populated_countries(file_path:str, quantity:int):
	countries_list = []
	with open(file_path, "r", encoding="UTF-8") as file:
		countries_list = json.load(file)

	countries_sorted = sorted(countries_list, key=lambda item: item["population"], reverse = True)

	most_populated = []

	for i in range(quantity):
		country = {
			"country": countries_sorted[i]["name"],
			"population": countries_sorted[i]["population"]
		}
		most_populated.append(country)
	
	return most_populated

print(most_populated_countries(countries_path,10))