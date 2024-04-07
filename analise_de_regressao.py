import main
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt

class AnaliseRegressao(main.AnaliseDataset):
    def __init__(self):
        super().__init__()

    def regressao_simples(self, x_col, y_col):
        y = self.df[y_col]
        X = self.df[x_col]
        X = sm.add_constant(X)
        modelo = sm.OLS(y, X)
        resultado = modelo.fit()
        print(resultado.summary())
        plt.figure(figsize=(12, 8))
        plt.xlabel(x_col, size=16)
        plt.ylabel(y_col, size=16)
        plt.plot(X[x_col], y, "o", label="Dados Reais")
        plt.plot(X[x_col], resultado.fittedvalues, "r-", label="Linha de Regressão (Previsões do Modelo)")
        plt.legend(loc="best")
        plt.show()

if __name__ == '__main__':

    grafico = AnaliseRegressao()
    grafico.regressao_simples('area_m2', 'valor_aluguel')
