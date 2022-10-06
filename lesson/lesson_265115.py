"""
print('"Python is a great language!", said Fred. "I don'+"'t ever remember having this much fun before."+'"')

name, surname = input(), input()
print(f'Hello {name} {surname}! You just delved into Python')

command = input()
print(f'Футбольная команда {command} имеет длину {len(command)} символов')

city = [input() for x in range(3)]
city.sort(key=len)
print(city[0], city[2], sep='\n')

x = [len(input()) for _ in range(3)]
x.sort()
res = 'NO'
if x[0] - x[1] == x[1] - x[2]:
    res = 'YES'
print(res)

str = input()
if 'синий' in str:
    print('YES')
else:
    print('NO')

str = input()
if 'суббота' in str or 'воскресенье' in str:
    print('YES')
else:
    print('NO')

text = input()
print("YES" if any(day in text for day in ["суббота", "воскресенье"]) else 'NO')
"""
text = input()
if '.' in text and '@' in text:
    print('YES')
else:
    print('NO')
