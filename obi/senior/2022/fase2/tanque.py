c = int(input())
d = int(input())
t = int(input())

litros_aeroporto = d/c

if t >= litros_aeroporto:
  abastecimento = 0
else:
  abastecimento = litros_aeroporto - t

print(f"{abastecimento:.1f}")

'''
2
10
0

5.0

30
100
2

1.3

50
120
3

0.0

100
146
0

1.5

'''