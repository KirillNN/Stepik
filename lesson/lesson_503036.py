'''
# step 10
def count_args(*args):
    return len(args)

# step 11
def sq_sum(*args):
    return sum([x ** 2 for x in args])


print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# step 12
def mean(*args):
    data = [x for x in args if type(x) in (int, float)]
    return sum(data) / len(data) if data else 0.0


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# step 13
def greet(name, *args):
    names = (name, *args)
    result = ' and '.join(names)
    return f'Hello, {result}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))

# step 14
def print_products(*args):
    products = [x for x in args if type(x) is str and len(x) > 0]
    if not products:
        print('Нет продуктов')
    result = []
    for index, product in enumerate(products, start=1):
        result.append(f'{index}) {product}')
    print('\n'.join(result))


print(print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True))
print(print_products([4], {}, 1, 2, {'Beegeek'}, ''))
'''


# step 15
def info_kwargs(**kwargs):
    kwargs = sorted(kwargs.items())
    for key, value in kwargs:
        print(f'{key}: {value}')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
