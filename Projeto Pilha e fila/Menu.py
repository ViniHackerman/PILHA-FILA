from queue import Queue
from collections import deque 
q = Queue()

def menu():
    print('-'*17)
    print('Seja bem - vindo')
    print('-'*17)
    print()
    print('[1] - Operações')
    print('[2] - Expressão')
    print('[3] - Finalizar Programa')
    print()
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print(menu_operacao())
    if opcao == 2:
        print(expressao())
    if opcao == 3:
        print('Programa finalizado!')


def menu_operacao():
    print('-'*10)
    print('Operações')
    print('-'*10)
    print()
    print('[1] - Adicionar operação na fila')
    print('[2] - Executar Próxima Operação da Fila')
    print('[3] - Executar Todas as Operações da Fila')
    print('[4] - Voltar para o menu principal')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        print(opfila())
    if opcao == 4:
        print(menu())





def expressao():
    print('expressao')





def opfila():
    print('-'*34)
    print('Escolha qual operação deseja usar')
    print('-'*34)
    print('[1] - Adição(+)')
    print('[2] - Subtração(-)')
    print('[3] - Multiplicação(*)')
    print('[4] - Divisão(/)')
    ope = int(input('Escreva o numero de sua operação: '))
    if ope == 1:
        print(adi())
    if ope == 2:
        print(sub())
    if ope == 3:
        print(mult())
    if ope == 4:
        print(div())





def adi():
     numeros = (input('Escreva os numeros com um espaço entre eles: '))
     numeros = numeros.split()
     for i in numeros:
         inte = int(i)
         q.put(inte)
         
     print(f'Adição = {q.queue}')
     soma = sum(q.queue)
     print(f'O resultado da soma foi de: {soma}')

def sub():
    numeros = input('Escreva os números com um espaço entre eles: ')
    numeros = numeros.split()
    for i in numeros:
      inte = int(i)
      q.put(inte)

    print(f'Subtração = {q.queue}')
    resultado = q.get()
    while not q.empty():
      resultado -= q.get()
    print(f'O resultado da subtração é: {resultado}')


def mult():
    numeros = input('Escreva os números com um espaço entre eles: ')
    numeros = numeros.split()
    for i in numeros:
      inte = int(i)
      q.put(inte)
    print(f'Multiplicação = {q.queue}')
    resultado = q.get()
    while not q.empty():
      resultado = resultado * q.get()
    print(f'O resultado da multiplicação é: {resultado}')


def div():
    numeros = input('Escreva os números com um espaço entre eles: ')
    numeros = numeros.split()
    for i in numeros:
        inte = int(i)
        q.put(inte)
    print(f'Divisão = {q.queue}')
    resultado = q.get()
    while not q.empty():
      resultado = resultado / q.get()
    print(f'O resultado da divisão é: {resultado}')


menu()