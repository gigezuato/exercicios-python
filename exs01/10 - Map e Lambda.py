idades = [18, 21, 16, 30, 15]

status = map(lambda idade: 'maior de idade' if idade >= 18 else 'menor de idade', idades)

print(list(status))