numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

multiplicacao = numero1 * numero2 * numero3
soma = numero1 + numero2 + numero3
subtracao = numero1 - numero2 - numero3
totalS = multiplicacao + soma + subtracao

print(f"A multiplicaçao entre {numero1}, {numero2} e {numero3} é: {multiplicacao}")
print(f"A soma entre {numero1}, {numero2} e {numero3} é: {soma}")
print(f"A subtracao entre {numero1}, {numero2} e {numero3} é: {subtracao}")
print(f"A soma total entre {multiplicacao}, {soma} e {subtracao} é: {totalS}")