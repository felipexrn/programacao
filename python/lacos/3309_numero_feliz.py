def feliz(num):
  if num == 1: return num
  else:
    while num != 1: # enquanto num não for 1
      if num == 4: # se num for igual a 4 ele para o laço
        break
      algarismos = []
      while num < 10: # eleva o num ao quadrado se menor que 10
        num = num**2
      while num//10 > 0: # separa os algarismos de num
        algarismos.append((num%10)**2) # eleva os algarismos de num ao quadrado
        num = num//10
        if num//10 == 0:
          algarismos.append((num%10)**2)
          break # aqui evito de passar novamente no while
      num = sum(algarismos)
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
