c = int(input())
for i in range(c):
  notas = list(map(int, input().split()))
  alunos = notas[0]
  del notas[0]
  media = sum(notas) / alunos
  notas_acima_media = [nota for nota in notas if nota > media]
  porcentagem_notas_acima_media = len(notas_acima_media)/len(notas)
  print(f"{porcentagem_notas_acima_media:.3%}")
  
'''
Casos de teste
Entrada:
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

Saída:
40.000%
57.143%
33.333%
66.667%
55.556%

'''
