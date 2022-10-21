import time
from subcadeias import sub_cadeias
pasta = 1
for a in range(10):
  arquivo = 1
  for b in range(4):
    teste = open(f"{pasta}/{arquivo}.in")
    n = int(teste.readline())
    cadeia = teste.readline()
    inicio = time.process_time()
    retorno = sub_cadeias(n, cadeia)
    fim = time.process_time()
    tempo = "{:.3f}".format(fim - inicio) + " segundos"
    resultado = open(f"{pasta}/{arquivo}.sol")
    if retorno == int(resultado.readline()):
      print(f"Arquivo {arquivo} da pasta {pasta} correto", "levou", tempo)
    else:
      print(f"Arquivo {arquivo} da pasta {pasta} errado", "levou", tempo)
    teste.close()
    resultado.close()
    arquivo += 1
  pasta += 1 
