def sub_cadeias(n, cadeia):
  
  '''
  n = int(input())
  cadeia = input()
  '''
  subcadeias = []
  palindromos = []
  
  
  for i in range(n):
    for j in range(i+1, n+1):
      subcadeias.append(cadeia[i:j])
  
  #for i in subcadeias:
  #  print(i)
  
  for i in subcadeias:
    sub = i
    metade = len(sub)//2
    if len(sub)%2 == 0:
      sub1 = sub[:metade]
      sub2 = sub[metade:]
    else:
      sub1 = sub[:metade]
      sub2 = sub[metade+1:]
    sub2 = sub2[::-1]
    
    if sub1 == sub2:
      palindromos.append(len(sub))
  
  return max(palindromos)
  
  '''
  
  15
  vovossorirmirim
  
  5
  
  8
  abxxxxba
  
  8
  
  '''