def get_leaf_year(year):
	if (year % 400 == 0):
		return "true"
	elif(year % 100 == 0):
		return "false"
	elif(year % 4 ==0):
		return "false"
	else:
		return "false"

def check_number(num):
	if (num % 2 == 0 or num == 0):
		return "jjaksu"
	else:
		return "holsu"

def get_yoil_index(year, month, day):

	day_adder = 0

	for year_f in range(1, year):
		if (get_leaf_year(year_f) == "true"):
			day_adder = day_adder + 366
		else:
			day_adder = day_adder + 365

	for month_f in range(1,month):
		check_leap = get_leaf_year(year)
		if (month_f == 2 and check_leap == "true"):
			day_adder = day_adder + 29

		elif (month_f == 2 and check_leap == "false"):
			day_adder = day_adder + 28

		elif (month_f == 7 ):
			day_adder = day_adder + 31

		elif (month_f == 8) :
			day_adder = day_adder + 31

		else:
			if (check_number(month_f) == "holsu"):
				day_adder = day_adder + 31

			else:
				day_adder = day_adder + 30

	
	day_adder = day_adder + day

	return day_adder % 7

def __main__():
	d = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	day = d[get_yoil_index(2016, 4, 16)]
	print("Today is: ", day)
	# print(check_number())




__main__()
