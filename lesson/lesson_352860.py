# step 5
# alphabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
#             "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

# alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
from string import ascii_lowercase as alphabet


def decode(text, shift):
    result = ""
    for i in text:
        if i.lower() in alphabet:
            index = alphabet.index(i.lower())
            new_index = (index + shift) % len(alphabet)
            if i.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += i
    return result


user_input = input().split()
output_list = []
for word in user_input:
    output_list.append(decode(word, len([x for x in word if x.isalpha()])))
print(' '.join(output_list))
