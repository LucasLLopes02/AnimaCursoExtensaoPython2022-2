#Peça o nome do aluno e sua nota (0 a 10) e, se ele tirou nota 10, mostra "Você é boladão..."
nome = input("Insira seu nome: ")
nota = float(input("Digite sua nota de 0 a 10: "))

if (nota == 10)
  print("{}, Você é boladão" .format(nome)) 
elif (nota >= 6 and nota < 10)
  print("{}, mediano em" .format(nome))
else:
  print("Você é bem burrinho amigo")