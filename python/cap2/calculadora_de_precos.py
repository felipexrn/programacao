quantidade = int(input())
preço = float(input())
total = quantidade*preço
print("O custo total é de R$ {:.2f}. A quantidade de {:d} produtos pelo preço de R$ {:.2f} cada".format(total, quantidade, preço))
