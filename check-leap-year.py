def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return f"{year} is a leap year"
            else:
                return f"{year} is not a leap year"
        else:
            return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

year = int(input("Enter a year: "))

print(is_leap(year))
