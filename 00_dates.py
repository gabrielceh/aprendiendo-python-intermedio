# Dates

# import datetime
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

print("\n" + ("*~" * 10), "datetime: Obtener fecha y hora actual" ,("*~" * 10))

now = datetime.now()

def print_datetime(date):
	print(f"now: {date}")
	print(f"now.year: {date.year}")
	print(f"now.month: {date.month}")
	print(f"now.day: {date.day}")
	print(f"now.hour: {date.hour}")
	print(f"now.minute: {date.minute}")
	print(f"now.second: {date.second}")
	print(f"now.timestamp(): {date.timestamp()}")
	print(f"{date.day}/{date.month}/{date.year}")
	print("++++++++++++++++++++++++++++++")

print_datetime(now)


print("\n" + ("*~" * 10), "datetime: Creando y Formateando fechas" ,("*~" * 10))

my_new_year = datetime(2024, 7, 14, 13)  # obligatorio(year, month, day), no obligatorio(hour, min, sec)
print_datetime(my_new_year)

def formating_time(date):
	t = date.strftime("%d/%m/%Y, %H:%M:%S")
	print(t)

formating_time(my_new_year)


print("\n" + ("*~" * 10), "datetime: time" ,("*~" * 10))

complete_time_default = time()
print(f"hora completa: {complete_time_default}")

def print_time(time):
	print(f"time(): {time}")
	print(f"time().hour {time.hour}")
	print(f"time().minute: {time.minute}")
	print(f"time().second: {time.second}")
	print(f"time().second: {time.microsecond}")
	print("+++++++++++")

print_time(complete_time_default)

custom_time = time(10,45,15)
print_time(custom_time)
custom_time = time(minute=12, microsecond=450, hour=16, second=30)
print_time(custom_time)



print("\n" + ("*~" * 10), "datetime: date" ,("*~" * 10))

default_date = date.today()

def print_date(date):
	print(f"date(): {date}")
	print(f"date().year: {date.year}")
	print(f"date().month: {date.month}")
	print(f"date().day: {date.day}")
	print(f"date().weekday(): {date.weekday()}")
	print(f"date().ctime(): {date.ctime()}")

	print("+++++++++++")

print_date(default_date)

custom_date = date(2023, 1, 2)
print_date(custom_date)


print("\n" + ("*~" * 10), "datetime: Operaciones entre fechas" ,("*~" * 10))
print("Usando date")
today= date.today()
my_birthday = date(2023, 7, 14)
time_left_for_my_birthday = my_birthday - today

print(time_left_for_my_birthday)

year = today.year
month = today.month
day = today.day
hour = now.hour
minutes = now.minute
seconds = now.second

print("usando datetime")
new_today = datetime(year = year, month = month, day=day, hour=hour, minute=minutes, second=seconds)
my_birthday_two = datetime(2023, 7, 14)
time_left_for_my_birthday = my_birthday_two - new_today
print(time_left_for_my_birthday)



print("\n" + ("*~" * 10), "datetime: timedelta" ,("*~" * 10))

time_delta = timedelta(weeks=50, days=3, hours=5, minutes=5)

print(time_delta)


