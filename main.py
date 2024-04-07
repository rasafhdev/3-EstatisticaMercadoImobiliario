import pandas as pd

class AnaliseDataset:
    def __init__(self):
        self.df = pd.read_csv('res/dataset.csv')

    def mensagem_colorida(self, mensagem, cor='\033[91m', negrito=True):
        negrito_code = '\033[1m' if negrito else ''
        reset_code = '\033[0m'
        return f"{negrito_code}{cor}{mensagem}{reset_code}"

    def verifica_ausentes(self):
        mensagem = self.mensagem_colorida('Contagem de Dados Ausentes:')
        print(f'\n{mensagem}\n{self.df.isna().sum()}')

    def mostra_correlacao(self):
        mensagem = self.mensagem_colorida('Correlação:')
        print(f'\n{mensagem}')
        print(self.df.corr())
    
    def informacoes_gerais(self):
        mensagem = self.mensagem_colorida('Informações Gerais:')
        print(f'\n{mensagem}')
        print(self.df.info())

if __name__ == '__main__':
    analisador = AnaliseDataset()
    analisador.verifica_ausentes()
    analisador.mostra_correlacao()
    analisador.informacoes_gerais()
