vowels_eng = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

word = input("Введите слово: ")

for letter in word:
    if letter in vowels_eng:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"В слове {word}: {vowel_count} гласных и {consonant_count} согласных букв")
print("Количество гласных букв в слове:")

for letter in vowels_eng:
    letter_count = word.count(letter)

    if letter_count == 0:
        text = False
    else:
        text = f"{letter_count} шт."

    print(f"'{letter}' - {text}")