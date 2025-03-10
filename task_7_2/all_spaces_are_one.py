text = "преобразовать    все идущие  подряд  пробелы   в    один"
new_text = ""
length_text = 1000

if len(text) < length_text:
    for i in range(len(text)):
        if text[i] != " ":
            new_text += text[i]
        else:
            if text[i + 1] != " ":
                new_text += " "

print(f"Исходный текст:\n {text}\n")
print(f"Преобразованный текст:\n {new_text}")
