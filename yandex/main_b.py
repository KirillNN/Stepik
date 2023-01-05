n = int(input())  # количество рядов в самолете
places = []
for _ in range(n):
    places.append(input())
# print(places)

m = int(input())  # количество групп пассажиров
passengers = []
for _ in range(m):
    num, side, position = input().split()
    passengers.append((int(num), side, position))


# print(passengers)


def print_places():
    for i in places:
        print(i)


for passenger in passengers:
    num, side, position = passenger
    # print(num, side, position)
    for i, place in enumerate(places):
        left, right = place.split('_')
        if num == 1 and side == 'left' and position == 'aisle':
            if left[2] == '.':
                print(f'Passengers can take seats: {i + 1}C')
                places[i] = left[:2] + 'X' + '_' + right
                print_places()
                places[i] = left[:2] + '#' + '_' + right
                break
        elif num == 1 and side == 'left' and position == 'window':
            if left[0] == '.':
                print(f'Passengers can take seats: {i + 1}A')
                places[i] = 'X' + left[1:] + '_' + right
                print_places()
                places[i] = '#' + left[1:] + '_' + right
                break
        elif num == 1 and side == 'right' and position == 'aisle':
            if right[0] == '.':
                print(f'Passengers can take seats: {i + 1}D')
                places[i] = left + '_' + 'X' + right[1:]
                print_places()
                places[i] = left + '_' + '#' + right[1:]
                break
        elif num == 1 and side == 'right' and position == 'window':
            if right[2] == '.':
                print(f'Passengers can take seats: {i + 1}F')
                places[i] = left + '_' + right[:2] + 'X'
                print_places()
                places[i] = left + '_' + right[:2] + '#'
                break
        elif num == 2 and side == 'left' and position == 'aisle':
            if left[1:] == '..':
                print(f'Passengers can take seats: {i + 1}B {i + 1}C')
                places[i] = left[0] + 'XX' + '_' + right
                print_places()
                places[i] = left[0] + '##' + '_' + right
                break
        elif num == 2 and side == 'left' and position == 'window':
            if left[:2] == '..':
                print(f'Passengers can take seats: {i + 1}A {i + 1}B')
                places[i] = 'XX' + left[2] + '_' + right
                print_places()
                places[i] = '##' + left[2] + '_' + right
                break
        elif num == 2 and side == 'right' and position == 'aisle':
            if right[:2] == '..':
                print(f'Passengers can take seats: {i + 1}D {i + 1}E')
                places[i] = left + '_' + 'XX' + right[2]
                print_places()
                places[i] = left + '_' + '##' + right[2]
                break
        elif num == 2 and side == 'right' and position == 'window':
            if right[1:] == '..':
                print(f'Passengers can take seats: {i + 1}E {i + 1}F')
                places[i] = left + '_' + right[0] + 'XX'
                print_places()
                places[i] = left + '_' + right[0] + '##'
                break
        elif num == 3 and side == 'left':
            if left == '...':
                print(f'Passengers can take seats: {i + 1}A {i + 1}B {i + 1}C')
                places[i] = 'XXX' + '_' + right
                print_places()
                places[i] = '###' + '_' + right
                break
        elif num == 3 and side == 'right':
            if right == '...':
                print(f'Passengers can take seats: {i + 1}D {i + 1}E {i + 1}F')
                places[i] = left + '_' + 'XXX'
                print_places()
                places[i] = left + '_' + '###'
                break
    else:
        print('Cannot fulfill passengers requirements')
