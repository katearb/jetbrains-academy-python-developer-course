num_cafes = {}
while True:
    name = input()
    if name == 'MEOW':
        break
    else:
        name = name.split(' ')
        num_cafes[int(name[1])] = name[0]
check = 0
for k, v in num_cafes.items():
    if k > check:
        check = k
    else:
        continue

print(num_cafes[check])
