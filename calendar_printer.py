days_in_month = int(input('How many days in a month?: '))
day_of_the_week = int(input('What day of the week does the month start number-wise ie monday = 1?: '))
days = ['M','T','W','T','F','S','S']

first_week = days[(day_of_the_week-1):]
remainder = days_in_month - (7-(day_of_the_week-1))


full_weeks = remainder // 7
days_left = remainder % 7

print(first_week)

for x in range(full_weeks):
    print(days)

print(days[:days_left])

