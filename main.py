import sys 
sys.path.append('vendas')
from registro import registrar_venda

def menu():
    while True:
        print("\n*************************************")
        print("Bem vindo(a) ao Sistema de vendas!")
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
        """ elif opcao == '2':
                relatorios.gerar_relatorio()
            elif opcao == '3':
                gerar_graficos.gerar_grafico_vendas()
            elif opcao == '4':
                print("Saindo do sistema.")
                break """
        
menu()