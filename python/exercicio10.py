nIndentificacao = int(input('Escreva seu número de identificaçao: '))
salarioFx = int(input(f"{nIndentificacao}, informe seu salário mensal: R$"))
nCarrosVendidos = int(input(f"{nIndentificacao}, informe quantos carros vendeu este mês? "))
recebidoCarroVendido = int(input(f"{nIndentificacao}, informe o quanto ganha por carro vendido: R$"))

salMensalT = salarioFx + (nCarrosVendidos * recebidoCarroVendido)
print(f"{nIndentificacao}, seu salario total neste mes é: R${salMensalT}")