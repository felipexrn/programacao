# resolvido 100%

fim = False
caso = 0
senha = ""
while not fim:
  try: # try e except são usados para lhe dar com EOF (fim do arquivo)
    caso += 1 # contador para impressão da saída 
    n = int(input())
    v = list(map(float, input().split())) # lista de oleosidade dos botões
    for i in range(n):
      maior_oleosidade = max(v)
      digito_senha = v.index(maior_oleosidade)
      senha += str(digito_senha) # monta a sequencia dos dígitos da senha
      v[digito_senha] = -1 # gambiarra para evidenciar o segundo maior número.
    print("Caso ", caso,": ", senha, sep="") # impressão da sáida
    senha = ""
  except:
    fim = True

'''
Casos de teste:

Entrada:
5
0.02 0.23 0.07 0.18 0.17 0.72 0.48 0.36 0.67 0.35
4
0.76 0.52 0.74 0.19 0.15 0.99 0.13 0.59 0.48 0.45
4
0.83 0.86 0.37 0.16 0.41 0.38 0.36 0.67 0.32 0.20

Saída:
Caso 1: 58679
Caso 2: 5027
Caso 3: 1074
'''
