def return_maximum_of_2(a: int, b: int):
    if a >= b:
        return a
    else:
        return b

max_num = return_maximum_of_2(2, 3)
print(max_num)
print(return_maximum_of_2(20, 50))