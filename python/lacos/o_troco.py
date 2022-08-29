t = int(input())
for i in range(t): # leitura de dados
  d, n = map(float, input().split())
  precos = list(map(float, input().split()))
  trocos = []
  
  for j in precos: # calculo de trocos
    ingrediente = j
    quantidade = d // ingrediente
    valor_a_pagar = quantidade * ingrediente
    troco = d - valor_a_pagar
    trocos.append(troco)
    
  trocos = [troco for troco in trocos if troco < d] # retirada de trocos acima do valor d
  
  if len(trocos) == 0: # verificação de existencia de troco
    print(f"{0:.2f}") 
  else: 
    print(f"{max(trocos):.2f}") # maior troco possível

#100%
'''
2
50 3
15 50 24.35
50 4
15 16.50 50 22.40

5.00
5.20

'''