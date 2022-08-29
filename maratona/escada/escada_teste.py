import time
from escada_funcao import fluxo
arquivo = 1
correto = 0
errado = 0
for a in range(58):
  teste = open(f"input/E_{arquivo}")
  
  n = int(teste.readline())
  tempo = []
  direcao = []
  for a in range(n):
    t, d = map(int, teste.readline().split())
    tempo.append(t)
    direcao.append(d)
    
  inicio = time.process_time()
  resposta = fluxo(n, tempo, direcao)
  fim = time.process_time()
  tempo = "{:.3f}".format(fim - inicio) + " segundos"
  
  resultado = open(f"output/E_{arquivo}")
  r = int(resultado.readline().rstrip())
  
  if resposta == r:
    print(f"Arquivo {arquivo} está correto,", "levou", tempo)
    correto += 1
  else:
    print(f"Arquivo {arquivo} está ERRADO,", "levou", tempo, "", end="")
    #resposta e resultado
    print(resposta, r,)
    errado += 1
    
  teste.close()
  resultado.close()
  arquivo += 1
if(errado > 0):
  print(str(int(correto/errado*100))+"%")
else:
  print(str(int(correto/correto)*100)+"%")
