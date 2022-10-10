def tra_dec_hex(lista):
  for n in lista:
    if n == 10:
      lista[lista.index(n)] = "A"
    elif n == 11:
      lista[lista.index(n)] = "B"
    elif n == 12:
      lista[lista.index(n)] = "C"
    elif n == 13:
      lista[lista.index(n)] = "D"
    elif n == 14:
      lista[lista.index(n)] = "E"
    elif n == 15:
      lista[lista.index(n)] = "F"
  return lista

def conv_dec_hex(dec):
  lista = []
  if dec//16 == 0:
    lista.append(dec)
  else:
    while dec > 0:
      lista.append(dec%16)
      dec = dec//16
  lista.reverse()
  return lista

def dec_hex(dec):
  return tra_dec_hex(conv_dec_hex(dec))

num = int(input())
num_conv = dec_hex(num)
print(*num_conv, sep="")