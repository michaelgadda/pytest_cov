
#in order to run this file use either:
#python michael_gadda_hw1.py 
#or 
#python3 michael_gadda_hw1.py

#And when prompted please enter a valid year ( x > 0)

def leap_year_test():
	year_str = input("Please enter a year greater than 0: ")
	year = int(year_str)
	if year <= 0:
		print("Let's try again...")
		return leap_year_test()
	else: 
		if year % 4 == 0:
			if year % 100 != 0: 
				print(f"{year} is a leap year")
			else: 
				if year % 400 == 0: 
					print(f"{year} is a leap year")
				else:
					print(f"{year} is not a leap year")
		else: 			
			print(f"{year} is not a leap year")