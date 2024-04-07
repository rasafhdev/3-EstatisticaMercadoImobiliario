import pandas as pd

# Pergunta 1

class AnaliseDataset:
    def __init__(self):
        self.df = pd.read_csv('res/dataset.csv')

    def verifica_ausentes(self):
        print(f'Contagem de Dados Ausentes:\n{self.df.isna().sum()}')

    def mostra_correlacao(self):
        print('\nCorrelação:')
        print(self.df.corr())

if __name__ == '__main__':

    analisador = AnaliseDataset()
    analisador.verifica_ausentes()
    analisador.mostra_correlacao()