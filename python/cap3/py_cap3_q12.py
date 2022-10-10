print("Digite o tamanho da rua e a distância entre postes separados por espaço")
tamanho_rua, distancia_poste = map(int, input().split())
distancia_postes_finais = tamanho_rua * 1000 % distancia_poste
quantidade_postes = tamanho_rua * 1000 // distancia_poste + 1
quantidade_postes -= (tamanho_rua * 1000 / distancia_poste % 1 // -1)
print(int(quantidade_postes), "poste(s)")
print(int(distancia_postes_finais), "metro(s)") # Python CAP3 Q12


print(((tamanho_rua * 1000 + distancia_poste - 1) // distancia_poste) + 1)
