# multiple of 3 - print fuzz
# multiple of 5 - print buzz
# multiple of 3&5 - print fizzbuzz

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else :
        print(num)


def multiply(a, b):
    return a * b

