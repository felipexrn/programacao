print("digite o valor final de venda do automóvel com impostos")
formato = "{:.2f}"
icms = 18 / 100
ipi = 13 / 100
pis = 1.4 / 100
cofins = 7.6 / 100
valor_com_impostos = float(input())
valor_sem_impostos = valor_com_impostos / (1 + icms + ipi + pis + cofins)
print("ICMS:", formato.format(valor_sem_impostos * icms))
print("IPI:", formato.format(valor_sem_impostos * ipi))
print("PIS:", formato.format(valor_sem_impostos * pis))
print("Cofins:", formato.format(valor_sem_impostos * cofins))
print("Valor sem impostos:", formato.format(valor_sem_impostos))
