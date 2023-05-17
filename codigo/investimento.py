import datetime

class Investimento:
    def __init__(self, codigo, data, quantidade, valor_unidade, tipo, taxa_corretagem):
        self.__codigo = codigo
        self.__data = data
        self.__quantidade = quantidade
        self.__valor_unidade = valor_unidade
        self.__tipo = tipo
        self.__taxa_corretagem = taxa_corretagem
        self.__valor_operacao = None
        self.__imposto  = None
        self.__valor_final = None
        self.valor_operacao()
        self.imposto()
        self.valor_final()

    def __str__(self):
        return f' {self.__codigo:6} | {self.__data.strftime("%d/%m/%Y")} | {self.__quantidade:10} | {round(self.__valor_unidade, 2):16} | {self.__tipo:6} | {self.__taxa_corretagem:20} | {round(self.__valor_operacao, 2):17} | {round(self.__valor_final, 2):11} |'

    @property
    def data(self):
        return self.__data
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def quantidade(self):
        return self.__quantidade
     
    @property 
    def valor_unidade(self):
        return self.__valor_unidade
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def taxa_corretagem(self):
        return self.__taxa_corretagem

    @property
    def valor_operacao_a(self):
        return self.__valor_operacao
    
    @property
    def imposto_a(self):
        return self.__imposto

    @property
    def valor_final_a(self):
        return self.__valor_final

    def valor_operacao(self):
        self.__valor_operacao = (self.__quantidade * self.__valor_unidade)
    
    def imposto(self):
        self.__imposto = 0.0003
    
    def valor_final(self):
        if self.__tipo == 'COMPRA':
            self.__valor_final = self.__valor_operacao + (self.__valor_operacao * self.__imposto) + self.__taxa_corretagem
        else:
            self.__valor_final = self.__valor_operacao - (self.__valor_operacao * self.__imposto) - self.__taxa_corretagem