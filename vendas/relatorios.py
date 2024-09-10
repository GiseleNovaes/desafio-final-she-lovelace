import csv
from collections import defaultdict

def gerar_relatorio():
    try:
        vendas_por_produto = defaultdict(int)
        vendas_por_data = defaultdict(float)
        
        with open('vendas/dados/vendas.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pular o cabeçalho, se houver
            for row in reader:
                produto, quantidade, preco, data = row
                quantidade = int(quantidade)
                preco = float(preco)
                
                vendas_por_produto[produto] += quantidade
                vendas_por_data[data] += preco
        
        produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
        total_vendas_por_produto = dict(vendas_por_produto)
        total_vendas_por_data = dict(vendas_por_data)
        
        print("\nRelatório de Vendas:")
        print("\nVendas por produto:")
        for produto, quantidade in total_vendas_por_produto.items():
            print(f"{produto}: {quantidade} unidades")
        
        print("\nVendas por data:")
        for data, total in total_vendas_por_data.items():
            print(f"{data}: R$ {total:.2f}")
        
        print(f"\nProduto mais vendido: {produto_mais_vendido}")
    
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o relatório: {e}")
