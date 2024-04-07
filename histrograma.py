import main
import seaborn as sns
import matplotlib.pyplot as plt 

class Histograma(main.AnaliseDataset):
    def __init__(self):
        super().__init__()

    def histrograma(self):
        sns.set_palette('magma')
        sns.histplot(
            data= self.df,
            x = 'valor_aluguel',
            kde= True
        )
        plt.show()

if __name__ == '__main__':
    graph = Histograma()
    graph.histrograma()