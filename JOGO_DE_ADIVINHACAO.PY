print("=================================")
print("Bem-vindo ao jogo de adivinhação!")
print("=================================")

numero_secreto = 13

numero_chute = input("Digite seu número: ")
print(f"Você digitou: ", numero_chute)
chute = int(numero_chute)

if (numero_secreto == chute):
        print("Você acertou!")
        print("Fim do jogo.") 
else: 
        print("Você errou!")
        print("Fim do jogo.")    

