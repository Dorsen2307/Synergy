pets = {}

def input_pet():
    """Ввод информации о питомце"""
    pet_name = input("Введите имя питомца: ")

    pets[pet_name] = {} # добавляем нашему питомцу словарь с его данными

    # запрашиваем информацию о питомце
    type_pet = input("Введите вид питомца: ")
    while True:
        age_pet = int(input("Введите возраст питомца: "))
        if age_pet < 0:
            print("Возраст не может быть отрицательным. Попробуйте снова.")
            continue
        break
    owner_name = input("Введите имя владельца: ")

    # добавляем информацию о питомце в словарь
    pets[pet_name] = {
        "Вид питомца": type_pet,
        "Возраст питомца": age_pet,
        "Имя владельца": owner_name
    }

def determine_age_label(age):
    """Определяет правильное окончание для слова 'год'"""
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return "года"
    else:
        return "лет"

# вводим информацию о питомце
input_pet()

# получаем информацию о питомце
pet_name = list(pets.keys())[0]
pet_info = pets[pet_name]
pet_type = list(pet_info.keys())[0]
pet_age = list(pet_info.keys())[1]
pet_owner = list(pet_info.keys())[2]

print(f"Это {pet_info[pet_type]} по кличке \"{pet_name}\". "
      f"{pet_age}: {pet_info[pet_age]} {determine_age_label(pet_info[pet_age])}."
      f"{pet_owner}: {pet_info[pet_owner]}.")