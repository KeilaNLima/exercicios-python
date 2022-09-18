listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input('um valor na posição{}:')))
    if c == 0:
       maior = menor = listanum[c]
    else:
      if listanum[c] > maior:
           maior = listanum[c]
      if listanum[c] < menor:
           menor = listanum[c]
print('' * 30)
print('voce digitou os valores{}'.format(listanum)) 
print('qual o maior valor digitado{}'.format(maior))
for i, v in enumerate(listanum):
    if v == maior:
     print('{}'.format(i)) 
print('o menor valor digitado{}'.format(menor))
for i, v in enumerate(listanum):
     if v == menor:
        print('{}'.format(i))
print('as poisições dos valores{}'.format(listanum))
  