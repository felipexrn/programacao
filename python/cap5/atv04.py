print("Digite a base salarial, a meta de vendas e as vendas realizadas separados por vírgula ','")
base, meta, vendas = map(float, input().split(","))
salario = base + vendas * 0.03
if vendas >= meta:
  salario = salario + 0.1 * (vendas - meta)
print("O valor do Salário é de R$", "{:.2f}".format(salario))