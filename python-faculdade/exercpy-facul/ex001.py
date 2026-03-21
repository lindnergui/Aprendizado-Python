#Conversor de temperaturas (F - C)
tempf = float(input('Digite o valor da temperatura em Fahreheit: '))
tempc = (tempf - 32) * 5/9
print(f'Sua temperatura em Celsius é igual a:  {tempc:.2f}C')