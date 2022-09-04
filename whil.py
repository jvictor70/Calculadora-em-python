
while True:

    num1=input('Digite um numero: ')
    num2=input('digite outro numero: ')
    operador=input('digite um operador: ')
    sair = input('deseja sair? [s]im ou [n]ão:')
    if sair=='s':
        break



    if not num1.isnumeric() or not num2.isnumeric():
        print('você precisa digitar um numero')
        continue

    num1=int(num1)
    num2=int(num2)

#+ - / *
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print (num1 - num2)
    if operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print (num1 * num2)

