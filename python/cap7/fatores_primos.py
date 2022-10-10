import sys # método para ampliar as recursões do código
sys.setrecursionlimit(100000)

#programa para fatorar um número por números primos

#leitura de dados
n = int(input())
contador = 0
divisor = 1
lista = []

#função para verificar se um número é primo
def nPrimo(n, d):
  ePrimo = True
  global contador
  if d <= n:
    if n % d == 0:
      contador += 1
    if contador <= 2 and n != 1:
      return nPrimo(n, d + 1)
    if contador > 2 or n==1:
      ePrimo = False
  contador = 0
  return ePrimo

#função para encontrar o próximo número primo 
def pPrimo(n, d):
  global divisor
  if not nPrimo(n, d):
    divisor += 1
    return pPrimo(n + 1, d)
  else:
    return(n)

#função para fatorar número em números primos
def fat(n):
  global lista, divisor
  if n > 1:
    if n % pPrimo(divisor, 1) == 0:
      lista.append(divisor)
      return fat(n // divisor)
    else:
      divisor += 1
      return fat(n)
  return lista

#gatilho do programa
print(fat(n))

