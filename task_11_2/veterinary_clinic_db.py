import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
    3: {
        "Муся": {
            "Вид питомца": "кошка",
            "Возраст питомца": 4,
            "Имя владельца": "Ксюша"
        },
    },
    4: {
        "Бобик": {
            "Вид питомца": "собака",
            "Возраст питомца": 3,
            "Имя владельца": "Иван"
        },
    },
    5: {
        "Кеша": {
            "Вид питомца": "волнистый попугай",
            "Возраст питомца": 1,
            "Имя владельца": "Сергей"
        },
    }
}
command = ''

def create():
    """Создает новую запись с информацией о питомце"""
    if len(pets) == 0:
        last = 0
    else:
        last = collections.deque(pets, maxlen=1)[0]

    pet_name = input("Введите имя питомца: ")

    pets[last + 1] = {}  # добавляем запись с ИД
    pets[last + 1][pet_name] = {}  # добавляем в ID запись с именем нашего питомца

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
    pets[last + 1][pet_name] = {
        "Вид питомца": type_pet,
        "Возраст питомца": age_pet,
        "Имя владельца": owner_name
    }

def read(ID):
    """Отображает информацию о запрашиваемом питомце"""
    id_pet = get_pet(ID) # Получаем информацию о питомце по ID

    if not id_pet:
        print("Запрашиваемого ID не существует!")
        return

    # получаем информацию о питомце
    pet_name = list(id_pet.keys())[0]
    pet_info = id_pet[pet_name]
    pet_type = list(pet_info.keys())[0]
    pet_age = list(pet_info.keys())[1]
    pet_owner = list(pet_info.keys())[2]

    print(f"{ID}. "
          f"Это {pet_info[pet_type]} по кличке \"{pet_name}\". "
          f"{pet_age}: {pet_info[pet_age]} {get_suffix(pet_info[pet_age])}. "
          f"{pet_owner}: {pet_info[pet_owner]}.")

def update(ID):
    """Обновляет информацию об указанном питомце"""
    id_pet = get_pet(ID)  # Получаем информацию о питомце по ID

    if not id_pet:
        print("Запрашиваемого ID не существует!")
        return

    # получаем информацию о питомце
    name_pet = list(id_pet.keys())[0]
    info_pet = id_pet[name_pet]
    type_pet = list(info_pet.keys())[0]
    age_pet = list(info_pet.keys())[1]
    owner_pet = list(info_pet.keys())[2]

    # запрашиваем имя питомца
    print(f"\nТекущее имя питомца: {name_pet}")
    new_pet_name = get_new_value(name_pet, "Введите новое имя питомца")

    pets[ID][new_pet_name] = {}  # изменяем имя нашего питомца по ID

    # запрашиваем информацию о питомце
    print(f"\nТекущий тип питомца: {info_pet[type_pet]}")
    new_type_pet = get_new_value(info_pet[type_pet], "Введите новый вид питомца")

    print(f"\nТекущий возраст питомца: {info_pet[age_pet]}")
    while True:
        new_age_pet = int(get_new_value(info_pet[age_pet], "Введите новый возраст питомца"))

        if new_age_pet < 0:
            print("Возраст не может быть отрицательным. Попробуйте снова.")
            continue
        break

    print(f"\nТекущее имя владельца питомца: {info_pet[owner_pet]}")
    new_owner_name = get_new_value(info_pet[owner_pet], "Введите новое имя владельца")

    # добавляем информацию о питомце в словарь
    pets[ID][new_pet_name] = {
        "Вид питомца": new_type_pet,
        "Возраст питомца": new_age_pet,
        "Имя владельца": new_owner_name
    }

def delete(ID):
    """Удаляет запись о существующем питомце"""
    if not get_pet(ID):
        print("Запрашиваемого ID не существует!")
        return

    pets.pop(ID)

    print(f"Запись №{ID} удалена.")

    reindexing() # производим переиндексацию БД

def get_suffix(age):
    """Определяет правильный суффикс для количества лет"""
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    """Получает информацию о питомце в виде словаря"""
    return pets[ID] if ID in pets.keys() else False

def pets_list():
    """Отображает весь список питомцев"""
    for i in pets.keys():
        read(i)

def get_new_value(current_value, prompt):
    new_value = input(f"{prompt}\n(ENTER - оставить старое значение): ")
    return new_value if new_value else current_value

def reindexing():
    """Переиндексирует ключи БД"""
    list_keys = list(pets.keys())

    for i in range(len(pets)):
        pets[i + 1] = pets.pop(list_keys[i])

while command != 'stop':
    print("\nСписок команд:\n"
          "  create - создать запись о питомце\n"
          "  read - вывести информацию о питомце на экран\n"
          "  read list - вывести информацию обо всех питомцах на экран\n"
          "  update - обновить информацию о питомце\n"
          "  delete - удалить запись о питомце\n"
          "  stop - выход\n"
          )
    command = input("Введите команду: ")

    if command == 'create':
        create()
    elif command == 'read':
        read(int(input("Введите ID: ")))
    elif command == 'read list':
        pets_list()
    elif command == 'update':
        update(int(input("Введите ID: ")))
    elif command == 'delete':
        delete(int(input("Введите ID: ")))