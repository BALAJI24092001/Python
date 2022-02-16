from datetime import datetime
print("Enter date of birth: ")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
now = datetime.now()
pday = now.day
pmonth = now.month
pyear = now.year
print(pyear)
age = pyear - year
print(age)
if(month <= pmonth):
    if(month == pmonth):
        if(day < pday):
            print("Age: ", age-1)
        else:
            print("Age: ", age)
    else:
        print("Age: ", age)
else:
    print("Age: ", age-1)
