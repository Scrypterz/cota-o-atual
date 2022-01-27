import requests
import datetime
from time import sleep

lista = ['(  )', '( ✔ )']

#Cotação Dolar
cotacao1 = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao1 = cotacao1.json()
cotacao_dolar = cotacao1['USDBRL']['bid']

#Cotação Euro
cotacao2 = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao2 = cotacao2.json()
cotacao_euro = cotacao2['EURBRL']['bid']

def menu_cotacoes():
    try:
        while True:
            menu = int(input('Quer saber como está o Dolar e o Euro hoje?\n\n'
                             f'1 - Sim {lista[0]}\n'
                             f'2 - Não {lista[0]}\n\n'
                             f'Selecione a sua escolha: '))
            if menu == 1:
                print('Sua resposta: \n\n'
                      f'1 - Sim {lista[1]}\n'
                      f'2 - Não {lista[0]}\n')
                break
            elif menu == 2:
                print('Sua resposta: \n\n'
                      f'1 - Sim {lista[0]}\n'
                      f'2 - Não {lista[1]}\n')
                exit('Aplicativo fechado.')
            else:
                print('Selecione a opção correta!')
    except ValueError:
        print('Por favor, inserir somente números!')
        return menu_cotacoes()

def dolar_autal():
    print('Carregando...')
    sleep(3)
    dia_atual = datetime.datetime.now()
    mostrar_data = dia_atual.strftime('%d/%m/%Y - %H:%M')
    print(f'Data de hoje: {mostrar_data}')
    print()
    print(f'USD atual: {cotacao_dolar}')

def euro_atual():
    print(f'EUR atual: {cotacao_euro}')

menu_cotacoes()
dolar_autal()
euro_atual()