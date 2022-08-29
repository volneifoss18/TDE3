altura = int(input('Informe a altura: '))
raio = int(input('Informe o raio: '))

areaLateral = 2*3.14 *(raio * altura)
areaBase = 3.14 * (raio**2)
areatotal = areaBase + areaLateral
latasNecessarias = (areatotal/3)/5
precoTotal = latasNecessarias * 150.00

print(f"A area total é: {areatotal}")
print(f'A quantidade necessaria de tinta é: {latasNecessarias}')
print(f"Para essa pintura voce gastará o total de: R${precoTotal}")