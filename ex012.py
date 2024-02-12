n = float(input('Qual o preço do produto? R$'))
desconto = (n * 5) / 100
final = n - desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(n, final))
