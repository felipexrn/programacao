# resolvido 100%

s = input()
notas = []
for i in range(len(s)):
  num = int(s[i])
  if i == len(s) - 1 and num != 0: # armazena o último número
    notas.append(num)
  elif num > 0 and s[i+1] != "0": # armazena nota > 0 e < 10
    notas.append(num)
  elif num == 1 and s[i+1] == "0": # armazena nota 10
    notas.append(10)
  else:
    pass
print(f"{sum(notas) / len(notas):.2f}")
'''
Casos de teste

Entrada
310110
Saída
6.00

Entrada
10910
Saída
9.67

Entrada
222222223
Saída
2.11
'''
