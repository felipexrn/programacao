print("Digite a distância e a velocidade separados por espaço")
distancia, velocidade = map(int, input().split())
horas = distancia // velocidade
minutos = int((distancia / velocidade - horas) * 60)
print(horas, minutos, sep = ":") # Python CAP3 Q11