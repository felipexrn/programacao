def converter_dec_binario(num):
  bin = []
  if num == 1:
    bin.append(num%2)
  while num // 2 != 0:
    bin.append(num % 2)
    num = num // 2
    if num // 2 == 0:
      bin.append(num % 2)
      break
  while len(bin) < 32:
    bin.append(0)
  return bin

def converter_bin_decimal(bin):
  dec = 0
  for i in range(len(bin)):
    if bin[i] != 0:
      dec += bin[i] * 2**i
  return dec

while True:
  try:
    a, b = map(int, input().split())
    bin_a = converter_dec_binario(a)
    bin_b = converter_dec_binario(b)
    bin_soma = []
    for i in range(len(bin_a)):
      if bin_a[i] != bin_b[i]:
        bin_soma.append(1)
      else:
        bin_soma.append(0)
    #print(bin_a)
    #print(bin_b)
    #print(bin_soma) 
    dec_soma = converter_bin_decimal(bin_soma)
    print(dec_soma)
  except:
      break
#100%
'''
1 1
1 2
2 2
2 3
3 3
4 1
1 4
10 10
21 10
21 14
123 321
0 0
2863311530 1431655765
4294967295 4294967295

0
3
0
1
0
5
5
0
31
27
314
0
4294967295
0
'''