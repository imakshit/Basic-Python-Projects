import calendar


x  = int(input(print("enter year: ")))

y = int(input(print("Enter month: ")))

print(calendar.month(x , y))#prints the calendar for specific month and year

print("\n ------------------------------------------------------------------\n")


print(calendar.isleap(x))#returns true if the input year is a leap year

print("\n ------------------------------------------------------------------\n")


print(calendar.calendar(x))#prints the calendar for given year

