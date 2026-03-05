def Leia():
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    op = input('Digite a Operação [* / + -]: ')
    msg = f'{v1} {op} {v2}'
    if op == '+':
        res = Soma(v1,v2)
    elif op == '-':
        res = Subtração(v1,v2)
    elif op == '*':
        res = Multiplicação(v1,v2)
    elif op =='/':
        res = Divisão(v1, v2)
    Escreva(msg, res)        

def Soma (v1, v2):
    return (v1+v2)

def Subtração (v1, v2):
    return (v1-v2)

def Multiplicação (v1, v2):
    return (v1*v2)

def Divisão (v1, v2):
    if v2 == 0:
        raise ZeroDivisionError
    return (v1/v2)

def Escreva(msg, resultado):
    print(f'{msg} = {resultado}') 

try:
    Leia()
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except:
    print('Digite apenas números válidos!')