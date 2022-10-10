print("Digite o valor do salário e a porcentagem de reajuste separados por espaço")
salario, reajuste = map(float, input().split())
print("Atual:" + "{:.2f}".format(salario))
print("Novo:" + "{:.2f}".format(salario + (salario * reajuste / 100)))