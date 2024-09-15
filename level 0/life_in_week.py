age = input('What is u current age?')

age_as_int = int(age)

age_remaining = 90 - age_as_int
day_remaining = age_remaining * 365
weeks_remaining = age_remaining * 52
months_remaining = age_remaining * 12
year_remaining = months_remaining / 12

print(f"You have {day_remaining} days, {weeks_remaining} weeks, {months_remaining} months, {year_remaining} years left.")
