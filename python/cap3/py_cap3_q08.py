print("Digite o início e o fim do evento em minutos separados por espaço")
inicio, fim = map(int, input().split())
duracao = fim - inicio
horas = duracao // 60
minutos = duracao % 60
print(horas, minutos, sep = ":") # Python_CAP03_Q08