# parte 1: coleta de dados
nome = input("qual o seu nome?\n")
salario_bruto = float(input("qual o seu salario bruto (sem os desencontros)?\n"))

#parte 2: calculo dos descontos obrigatórios 
INSS = None
if salario_bruto <= 1212:
  INSS = 0.075 * salario_bruto
elif salario_bruto > 1212 and salario_bruto <= 2427.35:
  INSS = 0.09 * salario_bruto
elif salario_bruto > 2427.35 and salario_bruto <= 3641.03:
  INSS = 0.12 * salario_bruto
elif salario_bruto > 3641.03:
  INSS = 0.14 * salario_bruto


# IRRF
if salario_bruto <= 1903.98:
  IRRF = 0
elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
  IRRF = (0.075 * salario_bruto) - 142.80
elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
  IRRF = (0.15 * salario_bruto) - 354.80
elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
  IRRF = (0.225 * salario_bruto) - 636.13
else:
  IRRF = (0.275 * salario_bruto) - 869.36

#parte 3: no final tu vai subtrair o salário pelo descontos

salario_liquido = salario_bruto - INSS - IRRF

print(f"Certo, {nome}, seu salário líquido é de: R${salario_liquido:.2f}")
  
  