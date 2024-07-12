'''
# step 15
def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return (f'To: {mail}\n'
            f'Приветствую, {name}!\n'
            f'Вам назначен экзамен, который пройдет {date}, в {time}.\n'
            f'По адресу: {place}.\n'
            f'Экзамен будет проводить {teacher} в кабинете {number}.\n'
            f'Желаем удачи на экзамене!')
'''


# step 16
def pretty_print(data, side='-', delimiter='|'):
    length = sum(len(str(i)) + 2 for i in data) + len(data) - 1
    print(f' {side * length} ')
    string = f' {delimiter} '.join(map(str, data))
    print(f'{delimiter} {string} {delimiter}')
    print(f' {side * length} ')


pretty_print(['abc', 'def', 'ghi'], delimiter='#')
