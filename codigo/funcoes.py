import datetime

def digitos(info):
    if info == 'codigo':
        while True:
            try:
                codigo = input('\nDigite o código do investimento: ').upper()
                if not codigo[:3].isalpha() or not codigo[4:].isnumeric() and len(codigo) < 5 or len(codigo) > 5:
                    raise Exception
                return codigo
            except:
                print('\nCódigo inválido. Tente novamente!')

    elif info == 'data':
        while True:
            try:
                data = input('\nDigite a data do investimento: ')
                data_convertida = datetime.datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
                return data_convertida
            except:
                print('\nData inválida. Tente novamente!')

    elif info == 'quantidade':
        while True:
            try:
                quantidade = int(input('\nDigite a quantidade do investimento: '))
                if quantidade < 1:
                    raise Exception
                return quantidade
            except:
                print('\nQuantidade inválida. Tente novamente!')

    elif info == 'valor_unidade':
        while True:
            try:
                valor_unidade = float(input('\nDigite o valor da unidade do investimento: '))
                if valor_unidade <= 0:
                    raise Exception
                return valor_unidade
            except:
                print('\nValor inválido. Tente novamente!')

    elif info == 'tipo':
        while True:
            try:
                tipo = input('\nDigite o tipo do investimento: ').upper().strip()
                if tipo != 'COMPRA' and tipo != 'VENDA':
                    raise Exception
                return tipo
            except:
                print('\nTipo inválido. Tente novamente!')

    elif info == 'taxa_de_corretagem':
        while True:
            try:
                taxa_de_corretagem = float(input('\nDigite a taxa de corretagem do investimento: '))
                if taxa_de_corretagem <= 0:
                    raise Exception
                return taxa_de_corretagem
            except:
                print('\nValor da taxa inválido. Tente novamente!')

    elif info == 'escolha':
        while True:
            try:
                escolha = int(input('\nDigite sua escolha: '))
                if escolha < 0 or escolha > 6:
                    raise Exception
                return escolha
            except:
                print('\nEscolha inválida. Tente novamente!')

def menu():
    return '\n[1]_ Criar investimento. [2]_ Modificar investimento. [3]_ Listar investimentos. [4]_ Deletar investimento. [5]_ Detalhar ativo. [6]_Lucro/prejuízo da carteira. [0]_ Finalizar.'

def legenda_investimento(ativo):
    if ativo == None:
        return '____________________________________________________________________________________________________________________________\nID| CÓDIGO  |    DATA    | QUANTIDADE | VALOR DA UNIDADE |  TIPO  |  TAXA DE CORRETAGEM  | VALOR DA OPERAÇÃO | VALOR TOTAL |'
    else:
        return '_________________________________________________________________________________________________________________________________________\nID| CÓDIGO  |    DATA    | QUANTIDADE | VALOR DA UNIDADE |  TIPO  |  TAXA DE CORRETAGEM  | VALOR DA OPERAÇÃO | VALOR TOTAL | PREÇO MÉDIO |'

def linhas_horizontais(ativo):
    if ativo == None:
        return '--+---------+------------+------------+------------------+--------+----------------------+-------------------+-------------+'
    else:
        return '--+---------+------------+------------+------------------+--------+----------------------+-------------------+-------------+-------------+'
    
def opcoes_de_mudanca():
    return '\n[1]_ Código. [2]_ Data [3]_ Quantidade. [4]_ Valor Unidade. [5]_ Tipo. [6]_ Taxa de Corretagem.'
