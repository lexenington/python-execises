# This is a program to convert Temparature from Celcius to Fahrenheit and vice versa
print("To enter temparature in Celsius type 'C' for Temparature in Fahrenheit enter 'F'")
temp_type = input("What type of Temparature? ")

if temp_type == "C" or temp_type == "c":
    temp_c = input("What is the temparature in Celcius? ")
    temp_f = (int(temp_c) * 9/5) + 32
    result = F"{temp_c} degrees celcius in Fahrenheit is {temp_f}"
    print(result)
elif temp_type == "F" or temp_type == "f":
    temp_f = input("What is the temparature in Fahrenheit? ")
    temp_c = (5/9) * (int(temp_f) - 32)
    result = f"{temp_f} degress fahrenheit in celsius is {temp_c}"
    print(result)
else:
    print("Hey dude follow the rules!!")
