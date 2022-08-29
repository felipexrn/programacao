n, m = map(int, input().split())
p1 = n
p2 = m

def eh_primo(num):
  primo = False
  while not primo: # repete enquanto não encontra um número primo
    if num == 2: # se for 2 para a repetição... Nem sei se é necessário
      break
    
    for i in range(2, num): # verifica se um número é primo
      if num%i == 0:
        break
      if i == num-1 and num%i != 0: # o pulo do gato: se até aqui num%i !=0 então num é primo
        primo = True
    
    if primo:
      break
    num -= 1
  return num

print(eh_primo(p1)*eh_primo(p2))
#100% Não faço ideia de como isso funciona \o/

'''

Amostras de entrada	Amostras de saída
10 15
91

50 100
4559

'''