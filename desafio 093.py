jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador:'))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou'))
for c in range(0, tot):
      partidas.append(int(input(f'gols na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum (partidas)
print(jogador)
print('-='* 30)
for k, v in jogador.items():
  print(f' o campo {k} o valor {v}')
print('-='* 30)
for i, v in enumerate (jogador['gols']):
      print(f' na partida {i} fez {v} gols')
print(f'foi um toatal de {jogador["total"]} gols')