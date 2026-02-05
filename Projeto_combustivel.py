tipo = input('Digite E para Etanol ou D para Diesel: ')
litros = float(input('Quantidade de litros: '))

preco_etanol = 1.70
preco_diesel = 2.00

if tipo == 'E':
  if litros <= 15:
    porcentagem_desconto = 0.02
  else:
    porcentagem_desconto = 0.04

    valor = (litros * preco_etanol) - (preco_etanol * litros * porcentagem_desconto)
    print(f'O valor a ser pago é {valor}')

elif tipo == 'D':
    if litros <= 15:
      porcentagem_desconto = 0.03
    else:
      porcentagem_desconto = 0.05

      valor = (litros * preco_diesel) - (preco_diesel * litros * porcentagem_desconto)
      print(f'O valor a ser pago é {valor}')