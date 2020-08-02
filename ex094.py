pessoa = dict()
lista_de_pessoas = list()
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = 'A'

    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('Valor incorreto. Tente novamente.')

    pessoa['idade'] = int(input('Idade: '))
    continuar = 'A'

    while continuar not in 'NnSs':
        continuar = str(input('Deseja continuar [S/N]?: ')).strip()[0]
        if continuar not in 'SsNs':
            print('Valor incorreto. Tente novamente.')

    lista_de_pessoas.append(pessoa.copy())

    if continuar in 'Nn':
        break

print('-='*30)
print(lista_de_pessoas)
print(f' - O grupo tem {len(lista_de_pessoas)} pessoas.')
media_idade = 0
mulheres = list()

for c in range(len(lista_de_pessoas)):
    media_idade += lista_de_pessoas[c]['idade']

    if lista_de_pessoas[c]['sexo'] == 'F':
        mulheres.append(lista_de_pessoas[c]['nome'])

media_idade /= len(lista_de_pessoas)

print(f' - A média de idade é de {media_idade:.2f} anos.')
print(' - As mulheres cadastradas foram:', end=' ')
for c in range(len(mulheres)-1):
    print(mulheres[c], end=', ')
print(mulheres[-1])

print(' - Lista de pessoas com idade acima da média:', end='\n\n')
chaves = list(lista_de_pessoas[0].keys())
for c in range(len(lista_de_pessoas)):
    if lista_de_pessoas[c]['idade'] > media_idade:
        print(f'{chaves[0]} = {lista_de_pessoas[c]["nome"]}; '
              f'{chaves[2]} = {lista_de_pessoas[c]["idade"]}; '
              f'{chaves[1]} = {lista_de_pessoas[c]["sexo"]}')
print('<< ENCERRADO >>')
