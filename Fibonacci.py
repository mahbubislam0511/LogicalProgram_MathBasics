def fibonacci(n):
    fib_series_list = []
    if n <= 0:
        return fib_series_list
    elif n == 1:
        fib_series_list.append(0)
    elif n == 2:
        fib_series_list.extend([0, 1])
    else:
        fib_series_list.extend([0, 1])
        for i in range(2, n):
            fib_series_list.append(fib_series_list[i - 1] + fib_series_list[i - 2])
    return fib_series_list


# Example usage:
num_terms = int(input("Enter a number : "))  # Change this value to generate Fibonacci series up to a different number of terms
fib_series = fibonacci(num_terms)
print("Fibonacci Series:")
print(fib_series)
