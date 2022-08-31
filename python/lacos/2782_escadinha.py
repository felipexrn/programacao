# resolvido 100%

n = int(input())
s = list(map(int, input().split()))
if  n <= 2: # para casos de listas com até tamnaho 2
  print(1)
else: # para listas com tamanho > 2 
  diferencas = [] 
  for i in range(n-1):
    diferencas.append(abs(s[i] - s[i+1])) # armazena as diferenças

  escadinha = 1
  for i in range(len(diferencas)-1):
    if diferencas[i] != diferencas[i+1]:
      escadinha += 1 # conta escadinhas 

  print(escadinha)
  
'''
Casos de teste

Entrada
8
1 1 1 3 5 4 8 12
Saída
4

Entrada
1
112
Saída
1

Entrada
5
11 -106 -223 -340 -457
Saída
1
'''
