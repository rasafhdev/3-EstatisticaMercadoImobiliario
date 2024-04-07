import main
import seaborn as sns
import statsmodels.api as sm

class AnaliseRegressao(main.AnaliseDataset):
    def __init__(self):
        super().__init__()
    
    def treina_modelo(self, y, X):
        y_data = self.df[y]
        X_data = self.df[X]
        X_data = sm.add_constant(X_data)
        self.modelo = sm.OLS(y_data, X_data)
        self.modelo.fit()
        resultado = self.modelo.fit()
        return resultado

if __name__ == '__main__':

    analisador = AnaliseRegressao()
    resultado = analisador.treina_modelo('valor_aluguel', 'area_m2')
    print(resultado.summary())

