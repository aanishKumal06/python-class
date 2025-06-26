import datetime

my_birth_date_time = datetime.datetime(2006, 12, 2)

formating = my_birth_date_time.strftime("%b %d %Y -> %a")
print(formating)

user_input = "12 Dec 2024"

date_object = datetime.datetime.strptime(user_input, "%d %b %Y")
print(date_object)

five_year_laters = date_object + datetime.timedelta(days=5 * 365)
print(five_year_laters)
