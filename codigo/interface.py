from investimento import *
from funcoes import digitos, menu, legenda_investimento, linhas_horizontais, opcoes_de_mudanca
import psycopg2

conn = psycopg2.connect(
    host="containers-us-west-143.railway.app",
    port = "7528",
    database="railway",
    user="postgres",
    password="5pI2W3vto01B6zH1qgxj"
)

cur = conn.cursor()

def lucro_total():
    lista_das_listas = []
    lucro_total = 0
    cur.execute(f"SELECT DISTINCT cod_investimento FROM investimento")
    codigos = cur.fetchall()
    for n in range(len(codigos)):
        objeto = []
        lista_atual = None
        cur.execute(f"SELECT * FROM investimento WHERE cod_investimento = '{codigos[n][0]}'")
        lista_atual = cur.fetchall()
        for j in range(len(lista_atual)):
            objeto.append(Investimento(lista_atual[j][0], lista_atual[j][1], lista_atual[j][2], float(lista_atual[j][3]), lista_atual[j][4], float(lista_atual[j][5])))
        lista_das_listas.append(objeto)
    for n in range(len(lista_das_listas)):
        preco_medio = 0
        quantidade_total = 0
        quantidade_passada = 0
        venda = 0
        for m in range(len(lista_das_listas[n])):
            if lista_das_listas[n][m].tipo == 'COMPRA' and m == 0:
                preco_medio = lista_das_listas[n][m].valor_final_a / lista_das_listas[n][m].quantidade
                quantidade_total += lista_das_listas[n][m].quantidade
                quantidade_passada += lista_das_listas[n][m].quantidade
            elif lista_das_listas[n][m].tipo == 'COMPRA':
                quantidade_total += lista_das_listas[n][m].quantidade
                preco_medio = (lista_das_listas[n][m].valor_final_a + (quantidade_passada * preco_medio)) / quantidade_total
                quantidade_passada += lista_das_listas[n][m].quantidade
            elif lista_das_listas[n][m].tipo == 'VENDA':
                venda += lista_das_listas[n][m].valor_final_a- preco_medio * lista_das_listas[n][m].quantidade
                quantidade_total -= lista_das_listas[n][m].quantidade
                quantidade_passada -= lista_das_listas[n][m].quantidade
        lucro_total += venda
    print(f'\nLucro total: {lucro_total:.2f}')
    
def listar_investimentos(ativo = None, uso = None):
    if ativo == None:
        lista = []
        cur.execute("SELECT * FROM investimento ORDER BY data")
        lista_nao_convertida = cur.fetchall()
        for n in range(len(lista_nao_convertida)):
            objeto = Investimento(lista_nao_convertida[n][0], lista_nao_convertida[n][1], lista_nao_convertida[n][2], float(lista_nao_convertida[n][3]), lista_nao_convertida[n][4], float(lista_nao_convertida[n][5]))
            lista.append(objeto)
        print(legenda_investimento(None))
        for n in range(len(lista)):
            print(linhas_horizontais(None))
            print(f'{(n + 1):2.0f}| {lista[n]}')
        if uso == 'modificar':
            return lista
    else:
        lista = []
        cur.execute(f"SELECT * FROM investimento WHERE cod_investimento = '{ativo}' ORDER BY data")
        lista_nao_convertida = cur.fetchall()
        for n in range(len(lista_nao_convertida)):
            objeto = Investimento(lista_nao_convertida[n][0], lista_nao_convertida[n][1], lista_nao_convertida[n][2], float(lista_nao_convertida[n][3]), lista_nao_convertida[n][4], float(lista_nao_convertida[n][5]))
            lista.append(objeto)
        print(legenda_investimento(1))
        preco_medio = 0
        quantidade_total = 0
        quantidade_passada = 0
        venda = 0
        for l in range(len(lista)):
            if lista[l].codigo == str(ativo):
                if lista[l].tipo == 'COMPRA' and l == 0:
                    preco_medio = lista[l].valor_final_a / lista[l].quantidade
                    quantidade_total += lista[l].quantidade
                    quantidade_passada += lista[l].quantidade
                elif lista[l].tipo == 'COMPRA':
                    quantidade_total += lista[l].quantidade
                    preco_medio = (lista[l].valor_final_a + (quantidade_passada * preco_medio)) / quantidade_total
                    quantidade_passada += lista[l].quantidade
                elif lista[l].tipo == 'VENDA':
                    venda += lista[l].valor_final_a - preco_medio * lista[l].quantidade
                    quantidade_total -= lista[l].quantidade
                    quantidade_passada -= lista[l].quantidade
                print(linhas_horizontais(ativo))
                if lista[l].tipo == 'VENDA':
                    print(f'{(l + 1):2.0f}| {lista[l]}        ---- |')
                else:
                    print(f'{(l + 1):2.0f}| {lista[l]} {preco_medio:11.2f} |')
        if venda < 0:
            print(f'\nPrejuízo de {abs(venda):.2f}.')
        else:
            print(f'\nLucro de {venda:.2f}.')

def criar_investimento():
    codigo = digitos('codigo')
    data = digitos('data')
    quantidade = digitos ('quantidade')
    valor_unidade = digitos ('valor_unidade')
    tipo = digitos('tipo')
    taxa_de_corretagem = digitos('taxa_de_corretagem')

    cur.execute(f"INSERT INTO investimento (cod_investimento, data, quantidade, valor_unidade, tipo_investimento, taxa_de_corretagem) VALUES ('{codigo}', '{data}', {str(quantidade)}, {str(valor_unidade)}, '{tipo}', {str(taxa_de_corretagem)})")

    conn.commit()

def modificar_deletar_investimento(uso):
    lista = []
    lista = listar_investimentos(None, 'modificar')
    if uso == 'modificar':
        while True:
            try:
                escolha = int(input('\nDigite o ID do investimento que deseja modificar: '))
                if escolha < 1 or escolha > (len(lista)):
                    raise Exception
                else:
                    break
            except:
                print('\nID inválido. Tente novamente!')
    elif uso == 'deletar':
        while True:
            try:
                escolha = int(input('\nDigite o ID do investimento que deseja deletar: '))
                if escolha < 1 or escolha > (len(lista)):
                    raise Exception
                else:
                    break
            except:
                print('\nID inválido. Tente novamente!')
    print(legenda_investimento(None))
    print(linhas_horizontais(None))
    print(f'NA| {lista[escolha - 1]}')
    if uso == 'modificar':
        print(opcoes_de_mudanca())
        escolha = digitos('escolha')
        if escolha == 1:
            nov_codigo = digitos('codigo')
            cur.execute(f"UPDATE investimento SET cod_investimento = '{nov_codigo}' WHERE cod_investimento = '{lista[escolha - 1].codigo}' and data = '{lista[escolha - 1].data}' and quantidade = '{lista[escolha - 1].quantidade}' and valor_unidade = '{lista[escolha - 1].valor_unidade}' and tipo_investimento = '{lista[escolha - 1].tipo}' and taxa_de_corretagem = '{lista[escolha - 1].taxa_corretagem}'")
        elif escolha == 2:
            nov_data = digitos('data')
            cur.execute(f"UPDATE investimento SET data = '{nov_data}' WHERE cod_investimento = '{lista[escolha - 1].codigo}' and data = '{lista[escolha - 1].data}' and quantidade = '{lista[escolha - 1].quantidade}' and valor_unidade = '{lista[escolha - 1].valor_unidade}' and tipo_investimento = '{lista[escolha - 1].tipo}' and taxa_de_corretagem = '{lista[escolha - 1].taxa_corretagem}'")
        elif escolha == 3:
            nov_quantidade = digitos('quantidade')
            cur.execute(f"UPDATE investimento SET quantidade = '{nov_quantidade}' WHERE cod_investimento = '{lista[escolha - 1].codigo}' and data = '{lista[escolha - 1].data}' and quantidade = '{lista[escolha - 1].quantidade}' and valor_unidade = '{lista[escolha - 1].valor_unidade}' and tipo_investimento = '{lista[escolha - 1].tipo}' and taxa_de_corretagem = '{lista[escolha - 1].taxa_corretagem}'")
        elif escolha == 4:
            nov_valor_unidade = digitos('valor_unidade')
            cur.execute(f"UPDATE investimento SET valor_unidade = '{nov_valor_unidade}' WHERE cod_investimento = '{lista[escolha - 1].codigo}' and data = '{lista[escolha - 1].data}' and quantidade = '{lista[escolha - 1].quantidade}' and valor_unidade = '{lista[escolha - 1].valor_unidade}' and tipo_investimento = '{lista[escolha - 1].tipo}' and taxa_de_corretagem = '{lista[escolha - 1].taxa_corretagem}'")
        elif escolha == 5:
            nov_tipo = digitos('tipo')
            cur.execute(f"UPDATE investimento SET tipo_investimento = '{nov_tipo}' WHERE cod_investimento = '{lista[escolha - 1].codigo}' and data = '{lista[escolha - 1].data}' and quantidade = '{lista[escolha - 1].quantidade}' and valor_unidade = '{lista[escolha - 1].valor_unidade}' and tipo_investimento = '{lista[escolha - 1].tipo}' and taxa_de_corretagem = '{lista[escolha - 1].taxa_corretagem}'")
        elif escolha == 6:
            nov_taxa_de_corretagem = digitos('taxa_de_corretagem')
            cur.execute(f"UPDATE investimento SET cod_investimento = '{nov_taxa_de_corretagem}' WHERE cod_investimento = '{lista[escolha - 1].codigo}' and data = '{lista[escolha - 1].data}' and quantidade = '{lista[escolha - 1].quantidade}' and valor_unidade = '{lista[escolha - 1].valor_unidade}' and tipo_investimento = '{lista[escolha - 1].tipo}' and taxa_de_corretagem = '{lista[escolha - 1].taxa_corretagem}'")
    else:
        cur.execute(f"DELETE FROM investimento WHERE cod_investimento = '{lista[escolha - 1].codigo}' and data = '{lista[escolha - 1].data}' and quantidade = '{lista[escolha - 1].quantidade}' and valor_unidade = '{lista[escolha - 1].valor_unidade}' and tipo_investimento = '{lista[escolha - 1].tipo}' and taxa_de_corretagem = '{lista[escolha - 1].taxa_corretagem}'")

    conn.commit()

def main():
    while True:
        print(menu())
        
        escolha = digitos('escolha')

        if escolha == 1:
            criar_investimento()
        elif escolha == 2:
            modificar_deletar_investimento('modificar')
        elif escolha == 3:
            listar_investimentos()
            lucro_total()
        elif escolha == 4:
            modificar_deletar_investimento('deletar')
        elif escolha == 5:
            ativo = digitos('codigo')
            listar_investimentos(ativo)
        elif escolha == 6:
            lucro_total()
        elif escolha == 0:
            cur.close()
            conn.close()
            break

if __name__ == '__main__':
    main()
