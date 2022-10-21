# Cálculo de raiz quadrada através do método babilônico

import sys # método para ampliar as recursões do código
sys.setrecursionlimit(100)

#função para depuração
def debug(r0, rn, precisao, diferenca):
  print("r0", r0, "rn", rn)
  print("precisão", precisao,"diferenca", diferenca)
  print("p-d", precisao - diferenca, "\n")

# função para calcular a raiz
def raiz(x, r0, p): 
  rn = (r0 + (x/r0)) / 2
  precisao = 10**(-(p+1))
  diferenca = abs(r0-rn)
  #debug(r0, rn, precisao, diferenca)
  if precisao > diferenca:
    return r0 - diferenca
  else: return raiz(x, rn, p)

# Entrada de dados
x = int(input()) # número que será calculada a raíz quadrada
p = int(input()) # número de casas decimais da raiz
r0 = x / 2 # primeiro número candidato à raiz de x

# Saída de dados
formato = "{:."+str(p)+"f}"
print(formato.format(raiz(x, r0, p)))


'''

raiz(6, 3, 3)
ra = 3
rn = (3 + 6/3) / 2 == 2,5 

raiz(6, 2.5, 3)
ra = 2.5
rn = (2.5 + 6/2.5) / 2 == 2.45

raiz(6, 2.45, 3)
ra = 2.45
rn = (2.45 + 6/2.45) / 2 == 2.4494897959183675


'''