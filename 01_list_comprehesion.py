# List comprehesion

print("\n" + ("*~" * 10), "List comprehesion" ,("*~" * 10))

my_original_list = [0,1,2,3,4,5,6,7,8,9,10]
print(f"my_original_list: {my_original_list}")

list_range = list(range(11))
print(f"list_range: {list_range}")

list_comprehesion = [i for i in range(11)]
print(f"list_comprehesion: {list_comprehesion}")

list_double = [{i: i * 2} for i in range(11)]
print(f"list_double: {list_double}")

def mult_10(num):
	return num * 10

mult_list = [mult_10(i) for i in range(11)]
print(f"mult_list: {mult_list}")

list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = [number for row in list_of_list for number in row]
print(f"""
list_of_list: {list_of_list}
flat_list: {flat_list}
""")


print("\n" + ("*~" * 10), "List comprehesion con if" ,("*~" * 10))

even_numbers = [i for i in range(11) if i % 2 == 0]
print(f"even_numbers: {even_numbers}")

language = "Javascript"
no_a = [letter.lower() for letter in language if letter.lower() != 'a']
print(f"no a in javascript: {no_a}")
