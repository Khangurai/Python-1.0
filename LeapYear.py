#leapYear Program
print('To calculate leap Year \nEnter Year between 1900 and 2000 years:')

startYear = int(input('Start Year: '))
endYear = int(input('End Year: '))

print("Leap years between", startYear, "and", endYear, "are:")
leap_years_count = 0
for year in range(startYear, endYear + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, end='\n' if leap_years_count % 5 == 4 else ' ')
        leap_years_count += 1
        