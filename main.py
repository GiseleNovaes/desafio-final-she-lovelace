import os
import sys
from colorama import init, Fore

init(autoreset=True)

# Adiciona o diretório 'vendas' e 'graficos' ao caminho do módulo para importação
sys.path.append('vendas')
sys.path.append('graficos')

from registro import registrar_venda
from relatorios import gerar_relatorio
from gerar_graficos import gerar_grafico_vendas

def menu():
    while True:
        print("\n*************************************")
        print("Bem-vindo(a) ao Sistema de Vendas!")
        print("*************************************")
        opcao = input("""
        Escolha uma das opções abaixo:
        [1] para Registrar Vendas
        [2] para Gerar Relatórios
        [3] para Gerar Gráficos
        [4] para Sair
        Escolha uma opção: """)

        if opcao == '1':
            registrar_venda()
        elif opcao == '2':
            gerar_relatorio()
        elif opcao == '3':
            gerar_grafico_vendas()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print(Fore.RED + "Opção inválida. Por favor, digite um número válido entre 1 e 4.")

if __name__ == "__main__":
    # Cria o diretório de dados se não existir
    if not os.path.exists('vendas/dados'):
        os.makedirs('vendas/dados')
    
    menu()
