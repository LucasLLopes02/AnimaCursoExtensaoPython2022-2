# 1 comando de entrada input(): quero que o usuario digite algo
nome = input("Digite seu nome: ") 
#peça a idade para o usuário
idade = int(input("Qual sua idade? "))

#comando de saída.. exibir na tela
print("Boa Noite {}".format(nome))
#exiba sua idade é...
print("Sua idade é {} anos".format(idade))

#e se eu quiser mostrar o dobro da idade informada..
dobro = idade * 2
print("O dobro de sua idade é {}".format(dobro))
