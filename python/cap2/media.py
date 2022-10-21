n1,n2 = map(float, input().split())
media_ponderada = (n1*2+n2*3)/5
media_formatada = "{:.2f}".format(media_ponderada)
print(media_ponderada)
print(media_formatada)
