# Leap years occur according to the following formula: a leap year is divisible by four
print("Leap Year Finder \n")
year = int(input("What year do you want to check? "))

if (year % 4 == 0):
    result = f"Yes {year} is a leap year"
    print(result)
else:
    print("Sorry thats not a leap year")
