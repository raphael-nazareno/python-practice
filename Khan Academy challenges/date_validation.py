days_in_month = {
1: 31, 2: 28, 3: 31, 4: 30,
5: 31, 6: 30, 7: 31, 8: 31,
9: 30, 10: 31, 11: 30, 12: 31
}

day = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year: "))

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if day < 1 or day> 31:
    print("Error. Day must be between 1 and 31.")
elif month not in days_in_month:
        print("Error. Month must be between 1 and 12.")
elif year < 1000 or year> 9999:
    print("Error. Year must have four digits.")
elif year < 1926 or year > 2028:
    print("Error. Enter a valid year.")
else:
    max_days = days_in_month[month]

    if month == 2 and is_leap_year:
        max_days = 29

        if day > max_days:
            print("Error. That day does not exist in this month.")
        else:
            print("Valid date.")