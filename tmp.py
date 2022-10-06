"""
def is_magic(date):
    date = list(map(int, date.split('.')))
    if date[0] * date[1] == int(str(date[2])[2:]):
        return True
    else:
        return False
# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

Имеешь ввиду тесты?
1 Jackdaws love my big sphinx of quartz True
2 The five boxing wizards jump quickly True
3 The quick brown fox jumps over the lazy dog True
4 Crazy Fredrick bought many very exquisite opal jewels True
5 jsdfhsadfhkljsad False
6 Crazy Fredrick bought many very exquisite opal jewel True
7 razy Fredrick bought many very exquisite opal False

"""
from string import ascii_lowercase

# print(ascii_lowercase)


def is_pangram(text):
    return len(set(text.lower())) == 27


# считываем данные

# text = input()
text = 'jsdfhsadfhkljsad'

# вызываем функцию

print(is_pangram(text))
