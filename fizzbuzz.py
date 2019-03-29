# FizzBuzz Program! If a the input is divisible by 3 input should be Fizz if input is divisible by 5 then ouput should be Buzz. If output is divisible by 3 and 5 output should be FizzBuzz. If any other number then output should be the number


def FizzBuzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


print(FizzBuzz(15))
