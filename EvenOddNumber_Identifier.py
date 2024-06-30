
def even_odd_identifier(num_identifier):
    if num_identifier % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test the function
num1 = int(input("Enter a number: "))
print(f"The number {num1} is {even_odd_identifier(num1)}.")
