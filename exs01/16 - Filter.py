pessoas = [
    {"nome": "Ana", "idade": 17},
    {"nome": "Bruno", "idade": 21},
    {"nome": "Carla", "idade": 16},
    {"nome": "Daniel", "idade": 18},
    {"nome": "Eduarda", "idade": 20},
    {"nome": "Felipe", "idade": 15}
]

maiores = list(filter(lambda pessoa: pessoa['idade'] >= 18, pessoas))
print(maiores)