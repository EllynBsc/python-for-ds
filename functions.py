# def is_even(number):
#     return number % 2 == 0

# # execute the method with the argument number = 3
# print(is_even(3))


# def is_odd(number=0):
#     return number % 2 == 1

# print(is_odd())


def full_name(first_name, last_name, capitalize=False):
    if capitalize:
        return f"{first_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name} {last_name}"


print(full_name('david', 'last name', capitalize=True))
