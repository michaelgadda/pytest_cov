
#in order to run this file use either:
#python michael_gadda_hw1.py 
#or 
#python3 michael_gadda_hw1.py

#And when prompted please enter a valid year ( x > 0)

def leap_year_test(year):
	if year <= 0:
		print("Let's try again... Enter a number greater than 0")
		return False
	else: 
		if year % 4 == 0:
			if year % 100 != 0: 
				print(f"{year} is a leap year")
				return True
			else: 
				if year % 400 == 0: 
					print(f"{year} is a leap year")
					return True
				else:
					print(f"{year} is not a leap year")
					return False
		else: 			
			print(f"{year} is not a leap year")
			return False