#criação de funções

preco = 1999.90

#calcular 5% de imposto e guardar na variável imposto e exibir na tela

imposto = preco * 0.05
print(imposto)

#criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu
#Declaração da função
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto 

#Uso da função
preco = 299
valor_imposto = calcular_imposto(preco)
print(valor_imposto)

#calcular imposto desses 4 valores
valores = [1.99, 24.50, 78.27, 1515.5]

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")




def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")


