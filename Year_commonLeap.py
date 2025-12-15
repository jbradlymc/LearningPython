year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Common year")
