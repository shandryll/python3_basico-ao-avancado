for i in range(1, 11):
    print(f'i = {i}')

for j in range(10):
    print(f'j = {j}')

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')


palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')

aprovados = ['Ana', 'Zé', 'Mauro', 'Isa']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)
