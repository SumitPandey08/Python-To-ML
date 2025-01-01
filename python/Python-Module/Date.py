import datetime


now = datetime.datetime.now()
print(now)

sec = datetime.datetime.now().second
print(sec)

today = datetime.date.today()
print(today)

current_time = datetime.datetime.now().time()
print(current_time)

my_date = datetime.date(2025, 5, 1)  # Year, month, day
print(my_date)

formatted_date = my_date.strftime("%B %d, %Y")
print(formatted_date)  # Output: January 01, 2025

date_string = "01/01/2025"
parsed_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
print(parsed_date)




