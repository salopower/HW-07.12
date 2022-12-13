def change(lst):
    result = lst[:]
    result[0], result[-1] = result[-1], result[0]
    return result


print(change([2, 3, 5]))
