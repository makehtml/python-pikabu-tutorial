def calc(x, y):
    """Функция сложения."""
    return x + y


# result = calc(55, 23)
# result2 = calc(552, 231)

# print(result)
# print(result2)

def check_my_number(my_var_param, number_to_check):
    if my_var_param > number_to_check:
        print(f"{my_var_param} больше {number_to_check}")
    elif my_var_param < number_to_check:
        print(f"{my_var_param} меньше {number_to_check}")
    else:
        print(f"{my_var_param} равно {number_to_check}")


# my_var = 151
# check_my_number(my_var, 15)
