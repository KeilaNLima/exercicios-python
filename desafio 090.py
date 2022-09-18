 # Desafio 090

aluno = dict()
aluno['nome'] = str(input('nome: '))
aluno['média'] = float(input(f'Média {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'                        
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situção'] = 'reprovado'
print(aluno)
   


              