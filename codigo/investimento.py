class Investimento:
    def __init__(self, data, codigo, quantidade, valor_unidade, tipo, taxa_corretagem):
        self.__data = data
        self.__codigo = codigo
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
        return f'Código: {self.__codigo} | Data: {self.__data} | Quantidade: {self.__quantidade} | Valor da Unidade: {self.__valor_unidade} | Tipo: {self.__tipo} | Taxa de Corretagem: {self.__taxa_corretagem} | Valor da Operação: {self.__valor_operacao} | Imposto: {self.__imposto} | Valor Final: {self.__valor_final}'

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
    def codigo(self):
        return self.__valor_unidade
    
    @property
    def codigo(self):
        return self.__tipo
    
    @property
    def codigo(self):
        return self.__taxa_corretagem

    @property
    def codigo(self):
        return self.__valor_operacao
    
    @property
    def codigo(self):
        return self.__imposto

    @property
    def codigo(self):
        return self.__valor_final

    def valor_operacao(self):
        self.__valor_operacao = (self.__quantidade * self.__valor_unidade)
    
    def imposto(self):
        self.__imposto = 0.0003
    
    def valor_final(self):
        self.__valor_final = self.__valor_operacao + (self.__valor_operacao * self.__imposto) + self.__taxa_corretagem