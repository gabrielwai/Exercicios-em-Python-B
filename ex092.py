import datetime
dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
ano_atual = datetime.datetime.now().year
dicionario['idade'] = (ano_atual - int(input('Ano de nascimento: ')))
#print(dicionario["idade"])
dicionario['CTPS'] = str(input('Carteira de Trabalho (0 se não tem): '))

if dicionario['CTPS'] != '0':
    dicionario['contratação'] = int(input('Ano de Contratação: '))
    dicionario['salário'] = float(input('Salário: R$ '))
    dicionario['aposentadoria'] = (dicionario['contratação'] + 35) - (ano_atual - dicionario['idade'])
print('-='*30)                                # considerando 35 como padrão de contribuição para se aposentar
'''chaves = list(dicionario.keys())
print(chaves)'''

for k, v in dicionario.items():
    print(F' - {k} tem valor {v}')
