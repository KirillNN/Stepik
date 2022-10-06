ar = []
while True:
    text = input()
    if text != 'КОНЕЦ':
        ar.append(text)
    else:
        break
print(*ar, sep='\n')
