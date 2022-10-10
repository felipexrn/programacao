print("Digite uma coordenada cartesiana separada por vírgula e descubra a que quadrante o ponto pertence")
x, y = map(float, input().split(","))
print(x, y)
quadrante = ""

primeiro_quadrante = x > 0 && y > 0
segundo_quadrante = x < 0 and y > 0
terceiro_quadrante = x < 0 and y < 0
quarto_quadrante = x > 0 and y < 0
eixo_x = x == 0 and y != 0
eixo_y = x != 0 and y == 0
origem = x == 0 and y == 0 

if origem:
  quadrante = "Origem"
if eixo_x:
  quadrante = "Eixo X"
if eixo_y:
  quadrante = "Eixo Y"
if primeiro_quadrante:
  quadrante = "Primeiro quadrante"
if segundo_quadrante:
  quadrante = "Segundo quadrante"
if terceiro_quadrante:
  quadrante = "Terceiro quadrante"
if quarto_quadrante:
  quadrante = "Quarto quadrante"
print(quadrante)