# Problem 1

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Problem 2


def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year > 1582 and 0 < month <= 12:
        if month == 2 and is_year_leap(year):
            month_length[1] = 29

        return month_length[month - 1]

    else:
        return None


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 3, 12]
test_results = [28, 29, 31, 31]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Problem 3


def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year > 1582 and 0 < month <= 12:
        if month == 2 and is_year_leap(year):
            month_length[1] = 29

        return month_length[month - 1]

    else:
        return None


def day_of_year(year, month, day):
    if day > days_in_month(year, month) or day < 1:
        return None

    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)

    return total_days + day


print(day_of_year(2000, 12, 31))
print(day_of_year(1583, 2, 30))  # Invalid date
