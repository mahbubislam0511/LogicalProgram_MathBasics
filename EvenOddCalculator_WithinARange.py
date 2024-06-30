def count_even_odd(start_num, end_num):
    even_count = 0
    odd_count = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return even_count, odd_count


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

even, odd = count_even_odd(start, end)
print("Number of even numbers within the range:", even)
print("Number of odd numbers within the range:", odd)
