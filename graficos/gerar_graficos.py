import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_vendas():
    try:
        df = pd.read_csv('vendas/dados/vendas.csv', names=['produto', 'quantidade', 'preco', 'data'], header=None)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x='produto', y='quantidade')
        plt.xticks(rotation=45, ha='right')
        plt.title('Vendas por Produto')
        plt.xlabel('Produto')
        plt.ylabel('Quantidade Vendida')
        plt.tight_layout()
        plt.show()
    
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o gráfico: {e}")
