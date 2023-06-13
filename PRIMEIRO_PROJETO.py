#PROJETO BÁSICO DE CALCULADORA

print(40*"=")
print("Boas vindas ao meu primeiro projeto!")
print(40*"=")

nome = input("Digite seu nome: ")
print("Iniciando calculadora...")

print(f"Calculadora iniciada! E aí {nome} bora começar?")

continua = "S"
while(continua =="S"):
    num1 = float(input("Digite o primeiro número: "))
    op = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if(op == "+"):
        resultado = num1 + num2
    elif (op == "-"):
        resultado = num1 - num2
    elif (op == "*"):
        resultado = num1 * num2
    elif (op == "/"):
        resultado = num1 / num2
    else:
        resultado = 0

    print(f"Resultado: {resultado}")

    continua = input("Deseja continuar? (s/n): ")    