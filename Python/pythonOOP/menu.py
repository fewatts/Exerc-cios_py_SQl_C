from classes import *


def títulos(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    print('¬' * tam)


def menu():
    print(f'''1-Criar conta
2-Ver contas ativas
3-Verificar extrato
4-Depositar
5-Sacar
6-Transferir
7-Fechar sistema
''')


def criar_cliente():
    try:
        while True:
            dados = []
            dados.clear()
            try:
                dados.append(str(input('Nome: ')))
                dados.append(str(input('Sobrenome: ')))
                dados.append(str(input('CPF: ')))
            except:
                print('ERRO...')        
            for d in dados:
                print(f'{d}...', end='')
            resp = str(input('\nConfirma os dados? [S/N] ')).strip().upper()[0]
            if resp in 'S':
                cliente_0 = Cliente(dados[0], dados[1], dados[2])
                print('Dados Adicionados!')
                return cliente_0
    except:
        print('ERRO...')


def criar_conta(cliente):
    try:
        while True:
            dados = []
            dados.clear()
            try:
                dados.append(str(input('Nº da conta: ')))
                dados.append(cliente._nome)
                dados.append(float(input('SALDO: ')))
                dados.append(float(input('LIMITE: ')))
            except:
                print('ERRO...')
            for d in dados:
                print(f'{d}...', end='')
            resp = str(input('\nConfirma os dados? [S/N] ')).strip().upper()[0]
            if resp in 'S':
                conta_0 = Conta(dados[0], cliente, dados[2], dados[3])
                print('Dados Adicionados!')
                return conta_0
    except:
        print('ERRO...')

