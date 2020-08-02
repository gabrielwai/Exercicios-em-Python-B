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

    lista_de_pessoas.append(pessoa)

    if continuar in 'Nn':
        break

print(f'O grupo tem {len(lista_de_pessoas)} pessoas.')
media_idade = 0
for c in range(len(lista_de_pessoas)):
    media_idade += lista_de_pessoas[c]['idade']
print(f'A média de idade é de {media_idade} anos.')
print('As mulheres cadastradas foram:',end=' \n')
for c in range(len(lista_de_pessoas)):
    if lista_de_pessoas[]
    print(,end=' ')