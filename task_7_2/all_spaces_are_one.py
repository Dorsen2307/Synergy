text = "преобразовать    все идущие  подряд  пробелы   в    один"
new_text = ""
length_text = 1000

if len(text) < length_text:
    new_text = " ".join(text.split())

    print(f"Исходный текст:\n {text}\n")
    print(f"Преобразованный текст:\n {new_text}")
else:
    print(f"Преобразованный текст превышает {length_text} символов.")

