a, b = map(int, input().split())
resultado = 1
def exp(base, expoente):
  global resultado
  if expoente == 0:
    return 1
  else:
    resultado = base * exp(base, expoente - 1)
    return resultado

print(exp(a, b))

'''
2 10
1024

5 4
625
'''