salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('O novo salário desse funcionário, com aumento de 15% é de R${:.2f}.'.format(novo))