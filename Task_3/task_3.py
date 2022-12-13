def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


start_number = int(input("Enter start number: "))
end_number = int(input("Enter end number: "))
print(sum_range(start_number, end_number))
