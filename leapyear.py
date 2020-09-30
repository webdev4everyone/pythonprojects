year1 = int(input("Enter first year: ")) # Change 2019 to the year you wish to be the first
year2 = int(input("Enter second year: ")) # Change 2024 to the year you wish to be the first
if year1 % 4 == 0:
    print("Year 1 is a leap year") # If year 1 is div by 4 then it is a leap year.
else:
    print("Year 1 is not a leap year") # If year 1 is not div by 4 then it is not a leap year.
if year2 % 4 == 0:
    print("Year 2 is a leap year") # If year 2 is div by 4 then it is a leap year.
else:
    print("Year 2 is not a leap year") # If year 2 is not div by 4 then it is not a leap year.
