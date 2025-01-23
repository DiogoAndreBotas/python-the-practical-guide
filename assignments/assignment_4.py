def print_function(function):
    print(function())


def print_multiple_functions(*functions):
    for function in functions:
        print(f"{''.join([str(num) for num in function()]):^20}")


def list_of_numbers():
    return [1, 2, 3, 4, 5]


print_function(list_of_numbers)

print_function(lambda: [1, 2, 3, 4, 5])

print_multiple_functions(
    lambda: [1, 2, 3, 4, 5],
    lambda: [6, 7, 8, 9, 0],
    lambda: [7, 6, 5, 4, 3],
    lambda: [5, 6, 7, 8, 9]
)
