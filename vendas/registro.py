import csv
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

def registrar_venda():
    try:
        produto = input("Digite o nome do produto: ")
        qtd_prod = int(input("Digite a quantidade do produto: "))
        preco_produto = float(input("Digite o preço do produto: "))
        data_hora_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Adiciona a venda ao arquivo CSV
        with open('vendas/dados/vendas.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([produto, qtd_prod, preco_produto, data_hora_venda])
            print(Fore.GREEN + "Venda registrada com sucesso!")
    
    except Exception as e:
        print(Fore.RED + f"Ocorreu um erro: {e}")
