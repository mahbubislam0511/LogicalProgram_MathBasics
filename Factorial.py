def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


number = int(input("Enter a number to find its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    print(f"The factorial of {number} is {factorial(number)}.")
