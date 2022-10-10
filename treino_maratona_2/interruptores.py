n, m = map(int, input().split()) # interruptores e lâmpadas
acesas = list(map(int, input().split())) # lâmpadas acesas
del acesas[0]
lampadas = [lampada * 0 for lampada in range(m)]

for i in acesas:
  lampadas[i-1] = 1
interruptores = []

for i in range(n):
  interruptor = list(map(int, input().split()))
  del interruptor[0]
  interruptor = [lampada -1 for lampada in interruptor]
  interruptores.append(interruptor)

ciclo = 0
while sum(lampadas) > 0 and ciclo < 5:
  ciclo += 1
  for i in range(n):
    interruptor = interruptores[i]
    for j in interruptor:
      lampadas[j] = abs(lampadas[j] -1)

print(ciclo)