t, d, m  = map(int, input().split())
refeicoes = [0]
for a in range(m):
  refeicoes.append(int(input()))
refeicoes.append(d)

resposta = ""
'''
for a in range(len(refeicoes)-1):
  if refeicoes[a+1] - refeicoes[a] <= t:
    resposta = "Y" 
    break
  else:
    resposta = "N"
'''


if t<=d:
  if m>0:
    alimentou = False
    if refeicoes[0] < t:
      for b in refeicoes:
        if len(refeicoes) > 1 and refeicoes[1]-refeicoes[0] >= t:
          alimentou = True
          resposta = "Y" 
          break
        else:
          refeicoes = refeicoes[1:]
        if len(refeicoes) == 1 and d - refeicoes[0] >= t:
          alimentou = True
          resposta = "Y" 
          break
      if not alimentou:
        resposta = "N" 
    else:
      alimentou = True
      resposta = "Y" 
  else:
    alimentou = True
    resposta = "Y" 
else:
  resposta = "N" 
if t == d and d == m:
  alimentou = True
  resposta = "Y" 

print(resposta)

'''

Exemplo de entrada 1
3 10 3
2
4
7
Exemplo de sa´ıda 1
Y

Exemplo de entrada 2
4 10 3
2
4
7
Exemplo de sa´ıda 2
N

Exemplo de entrada 3
5 5 0
Exemplo de sa´ıda 3
Y

'''