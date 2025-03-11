my_dict = {i : i ** i for i in range(10, -6, -1)}

for i in range(len(my_dict)):
    print(f"{list(my_dict.keys())[i]} : {list(my_dict.values())[i]}")