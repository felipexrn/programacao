import time
from katmandu_funcao import viavel
arquivo = 1
correto = 0
errado = 0
for a in range(38):
  teste = open(f"input/K_{arquivo}.txt")
  
  t, d, m  = map(int, teste.readline().split())
  refeicoes = []
  for a in range(m):
    refeicoes.append(int(teste.readline()))
    
  inicio = time.process_time()
  resposta = viavel(t, d, m, refeicoes)
  fim = time.process_time()
  tempo = "{:.3f}".format(fim - inicio) + " segundos"
  
  resultado = open(f"output/K_{arquivo}")
  r = resultado.readline()

  print(resposta, r)
  if resposta == r:
    print(f"Arquivo {arquivo} está correto,", "levou", tempo)
    correto += 1
  else:
    print(f"Arquivo {arquivo} está ERRADO,", "levou", tempo)
    errado += 1
    
  teste.close()
  resultado.close()
  arquivo += 1
if(errado > 0):
  print(str(int(correto/errado*100))+"%")
else:
  print(str(int(correto/correto)*100)+"%")
