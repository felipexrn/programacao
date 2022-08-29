import time
from chuva import int_chuva
pasta = 1
for a in range(10):
  arquivo = 1
  for b in range(3):
    teste = open(f"{pasta}/{arquivo}.in")
    n = int(teste.readline())
    s = int(teste.readline())
    x = list(map(int, teste.readline().split()))
    inicio = time.process_time()
    intervalos = int_chuva(n, s, x)
    fim = time.process_time()
    tempo = "{:.3f}".format(fim - inicio) + " segundos"
    resultado = open(f"{pasta}/{arquivo}.sol")
    if intervalos == int(resultado.readline()):
      print(f"Arquivo {arquivo} da pasta {pasta} correto", "levou", tempo)
    else:
      print(f"Arquivo {arquivo} da pasta {pasta} errado", "levou", tempo)
    teste.close()
    resultado.close()
    arquivo += 1
  pasta += 1 
