# Desafio 095
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome:'))
    pessoa['sexo'] = str(input('sexo [M/F]:')).upper()[0]
    pessoa['idade'] = int(input('idade:'))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
      resp = str(input('quer continuar S/N:')).upper()[0]
      if resp  in 'S/N':
          break
    if resp == 'N':
      break
print('-=' * 30)
print(f'Ao todo temos {len(galera)}pessoas cadastrada')
media = soma / len(galera)
print(f'A media de idade {media:5.2f} ano.')
print (f'As mulheres cadastradas foram' ,end='')
for p in galera :
  if p ['sexo'] in 'Ff':
    print(f'{pessoa["nome"]}',end='')
print()
print('lista das pessoas que estão acima da media:')
for p in galera:
   if p ['idade'] >= media:
     print('  ')
     for k,v in p .items():
         print(f'{k} = {v}',end='')
     print(   )
print('<<encerrado<<')     
       
     
     
