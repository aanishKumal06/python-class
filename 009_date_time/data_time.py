import datetime

my_birth_date = datetime.date(2006, 12, 2)
print(my_birth_date)

five_year_before = my_birth_date - datetime.timedelta(days=5 * 365)
print(five_year_before)

my_birth_date_time = datetime.datetime(2006, 12, 2, 5, 0, 0)
print(my_birth_date_time)


before_time = my_birth_date_time - datetime.timedelta(hours=1, minutes=12, seconds=5, microseconds=12)
print(before_time)
# days, hours, minutes, seconds, microseconds
