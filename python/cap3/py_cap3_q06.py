print("Digite as duas notas separadas por espaço")
nota1, nota2 = map(int, input().split())
media_ponderada = int((nota1 * 2 + nota2 * 3) / 5)
print(media_ponderada) # Python_CAP3_Q06