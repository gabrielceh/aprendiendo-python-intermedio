from datetime import datetime

now = datetime.now()

"""
1. Get the current day, month, year, hour, minute and timestamp from datetime module
"""
print("\n" + ("*~" * 10), "Ejercicio 1" ,("*~" * 10))

def ex_1(now):
	year = now.year
	month = now.month
	day = now.day
	hour = now.hour
	minute = now.minute
	second = now.second
	timestamp = now.timestamp()

	return {
		"year": year,
		"month": month,
		"day": day,
		"hour": hour,
		"minute" :minute,
		"second": second,
		"timestamp": timestamp
	}

print(ex_1(now))

"""
2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
"""
print("\n" + ("*~" * 10), "Ejercicio 2" ,("*~" * 10))

now_formated = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now_formated)

"""
3. Today is 5 December, 2019. Change this time string to time.
"""
print("\n" + ("*~" * 10), "Ejercicio 3" ,("*~" * 10))

date_str = "December 5, 2019"
date_obj = datetime.strptime(date_str, "%B %d, %Y")
print(date_obj)

"""
4. Calculate the time difference between now and new year.
"""
print("\n" + ("*~" * 10), "Ejercicio 4" ,("*~" * 10))

new_year = datetime(2024, 1, 1)
time_to_new_year = new_year - now

print(time_to_new_year)

"""
5. Calculate the time difference between 1 January 1970 and now.
"""
print("\n" + ("*~" * 10), "Ejercicio 5" ,("*~" * 10))

today = datetime(2023, 2,  1)
year_1970 = datetime(1970, 1, 1, 19)
diff = today.timestamp() - year_1970.timestamp()
print(today.timestamp(), year_1970.timestamp())

minutes = diff / 60
hours = minutes / 60
days = hours / 24
months = days / 30
years = months / 12


print(diff)
print(minutes)
print(hours)
print(days)
print(months)
print(years)

