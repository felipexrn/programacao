def feliz(num):
  if num == 1: return num # retorna 1 se 1
  else:
    while num != 1 and num != 4: # enquanto num não for 1 ou 4
      algarismos = []
      while num < 10: # eleva o num ao quadrado se menor que 10
        if num**2 == 4:
          algarismos.append(num)
          break
        num = num**2
      while num//10 != 0: # separa os algarismos de num
        algarismos.append(num%10)
        num = num//10
        if num//10 == 0:
          algarismos.append(num%10)
          break # aqui evito de passar novamente no while
      if num != 4:
        for i in range(len(algarismos)):
          algarismos[i] = algarismos[i]**2 # eleva os algarismos de num ao quadrado
        num = sum(algarismos)
        #print(algarismos)
        #print(num, num**2)
        if num == 4: # se num for igual a 4 ele para o laço
          break
    return num  
    
n = int(input())
x = list(map(int, input().split()))

num_feliz = 0
for i in x:
  if feliz(i) == 1:
    num_feliz += 1

print(num_feliz)

# time limit exceeded ou 100% Vai entender

'''
10
1 2 3 4 5 6 7 8 9 10

3

4
2 4 29 12

0

3
2 3 5

0

'''