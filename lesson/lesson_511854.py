'''
# step 8
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if any([word in x for x in command.split()]):
            return True
    return False

# step 9
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

result = zip(countries, capitals, population)
print(*[f'{y} is the capital of {x}, population equal {z} people.' for x, y, z in result], sep='\n')

# step 10
abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))

data = zip(abscissas, ordinates, applicates)
print(all(x ** 2 + y ** 2 + z ** 2 <= 4 for x, y, z in data))

# step 11
ip = input().split('.')
if all(x.isdigit() for x in ip) and all(int(x) < 256 for x in ip):
    print(True)
else:
    print(False)

# step 12
print(*filter(lambda x: '0' not in str(x) and all(not x % int(i) for i in str(x)), range(int(input()), int(input()) + 1)))

# step 13
password = input()
result = any(map(lambda x: x.isdigit(), password)) and any(map(lambda x: x.isupper(), password)) and any(
    map(lambda x: x.islower(), password)) and len(password) > 6
print(['NO', 'YES'][result])
'''
# step 14
data = dict()
n = int(input())
for i in range(n):
    people = int(input())
    data[i] = []
    for _ in range(people):
        surname, grade = input().split()
        data[i].append(grade)
print(['NO', 'YES'][all('5' in x for x in data.values())])
