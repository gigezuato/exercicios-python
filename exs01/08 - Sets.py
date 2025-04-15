turma_a = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Isabela", "João"]

turma_b = ["Bruno", "Clara", "Diego", "Eduardo", "Fernanda", "Giovana", "Hugo", "Igor", "João", "Karen"]
a = set(turma_a)
b = set(turma_b)
interseccao = a.intersection(b)
apenas_a = a.difference(b)
uniao = a.union(b)
print('Alunos que estão nas duas turmas: ')
for aluno in interseccao:
    print(f'- {aluno}')
print('Alunos que estão apenas na turma A: ')
for aluno in apenas_a:
    print(f'- {aluno}')
print('Todos alunos únicos: ')
for aluno in uniao:
    print(f'- {aluno}')