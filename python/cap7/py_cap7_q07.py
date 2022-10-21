p_bim = list(map(int, input().split()))
s_bim = list(map(int, input().split()))

def media_final(n1, n2):
  return (n1 * 2 + n2 * 3) / 5

def n1(p_bim):
  l = p_bim[0]
  p_bim.pop(0)
  menor = min(p_bim)
  p_bim.remove(menor)
  a = sum(p_bim) / 2
  return l*50/100 + a*50/100

def n2(s_bim):
  l = s_bim[0]
  s_bim.pop(0)
  menor = min(s_bim)
  maior = max(s_bim)
  s_bim.remove(menor)
  s_bim.remove(maior)
  a = sum(s_bim) / 3
  return l*20/100 + a*80/100 

media = media_final(n1(p_bim), n2(s_bim))

if media >= 60:
  print("APROVADO")
else:
  print("NÃO APROVADO")

'''
90 20 60 80
50 20 40 60 80 100

20 20 30 70
40 20 30 40 50 60
'''