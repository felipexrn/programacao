a, b = map(int, input().split())

def fat(numero):
  if numero == 0:
    return 1
  else:
    return numero * fat(numero - 1)

print(fat(a) + fat(b))
