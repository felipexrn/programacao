n = int(input())
m = int(input())
s = int(input())
i = m - n
j = []
resultado = -1
for a in range(i + 1):
  j.append(a + n)
for b in j:
  if b > 9:
    soma = 0
    num = b
    alg = str(num)
    alg = list(map(int, alg))
    soma = sum(alg)
    if soma == s:
      resultado = b
print(resultado)
