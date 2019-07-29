pessoa = {'nome': 'Ana',
          'idade': 38,
          'cursos': ['Inglês', 'Português']
          }

print(len(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))

########################################################################################################################

pessoa['idade'] = 44
pessoa['cursos'].append('Italiano')
print(pessoa)
print(pessoa.pop('idade'))

pessoa.update({'idade': 40, 'sexo': 'F'})
print(pessoa)

del pessoa['cursos']
print(pessoa)
