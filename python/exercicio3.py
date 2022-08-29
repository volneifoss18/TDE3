tempoGasto = int(input('Digite o tempo total de viagem em horas: '))
velocidadeM = int(input('qual a sua velociade media no percurso? '))

distancia = tempoGasto * velocidadeM
litroGasto = distancia/12

print(f"a distancia percorrida foi {distancia} e foram gastos {litroGasto} litros de gasolina")