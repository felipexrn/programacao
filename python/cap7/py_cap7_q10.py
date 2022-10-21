numero = input()
digitos = [0,0,0,0,0,0,0,0,0,0]
contador = 0

def separa_digitos(numero):
  global digitos
  lista_digitos_num = list(numero)
  alg = len(lista_digitos_num)
  if alg > 0:
    digitos[int(lista_digitos_num[0])] += 1
    lista_digitos_num.pop(0)
    separa_digitos(numero[1:])

def resultado(): 
  global contador
  if contador < 10:
    print(f"{contador}:", digitos[contador])
    contador += 1
    return resultado()
  
def conta_digitos(n,d):
  return

separa_digitos(numero)
resultado()

'''
12341
0: 0
1: 2
2: 1
3: 1
4: 1
5: 0
6: 0
7: 0
8: 0
9: 0

8192
0: 0
1: 1
2: 1
3: 0
4: 0
5: 0
6: 0
7: 0
8: 1
9: 1

81921024901
0: 2
1: 3
2: 2
3: 0
4: 1
5: 0
6: 0
7: 0
8: 1
9: 2  
'''