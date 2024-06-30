def even_odd_list(start_num, end_num):
    even_numbers = []
    odd_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

even, odd = even_odd_list(start, end)
print("Even numbers within the range:", even)
print("Odd numbers within the range:", odd)
