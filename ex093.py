jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(jogador['partidas']):
    gols.append(int(input(f"Quantos gols na partida {c+1}?: ")))
jogador['gols'] = gols.copy()
del gols
print("-="*30)

'''for c in range(jogador['partidas']):
    print(jogador['gols'][c])'''# mostra os gols para cada partida jogada
jogador['total de gols'] = sum(jogador['gols'])
print(jogador)
print("-="*30)

chaves = list(jogador.keys())
valores = list(jogador.values())
for c in range(4):
    print(f'O campo {chaves[c]} tem o valor {valores[c]}.')
'''
    OU
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
'''
del chaves, valores
print("-="*30)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for c in range(jogador['partidas']):
    print(f"\t=> Na partida {c+1}, fez {jogador['gols'][c]} gols.")
'''
    OU
for i, v in enumerate(jogador["gols"]):
    print(f"\t=> Na partida {i}, fez {v} gols.")
'''
print(f"Foi um total de {jogador['total de gols']} gols.")
