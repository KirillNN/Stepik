# step 5
# alphabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
#             "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
# text = "Блажен, кто верует, тепло ему на свете!"
text = "To be, or not to be, that is the question!"
result = ""
for i in text:
    if i.lower() in alphabet:
        index = alphabet.index(i.lower())
        # print(index)
        new_index = (index + 17) % len(alphabet)
        if i.isupper():
            result += alphabet[new_index].upper()
        else:
            result += alphabet[new_index]
    else:
        result += i
print(result)
