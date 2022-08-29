print("Digite o valor do(s) produto(s) e a quantidade separados por ','")
valor, quantidade = map(float, input().split(","))
valor_e_maior = valor >= 500
quantidade_e_maior = quantidade >= 4
if valor_e_maior and quantidade_e_maior:
  valor = valor * 0.7 * quantidade
else:
  valor = valor * 0.9 * quantidade
print("O valor total é de R$", "{:.2f}".format(valor))