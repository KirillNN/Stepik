'''деление комплексных чисел'''
a = 2
b = 5
c = 3
d = 1
first = (a * c + b * d) / (c * c + d * d)
second = (b * c - a * d) / (c * c + d * d)
if second > 0:
    print(f'{first} + {second}i')
elif second < 0:
    print(f'{first} - {abs(second)}i')
else:
    print(first)


# (1+i)**3 = 1+2i-3
# (1+i)**2 = 1+2i-1
# 1+i+1+

