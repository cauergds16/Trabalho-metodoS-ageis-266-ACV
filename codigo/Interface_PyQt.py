import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from investimento import Investimento

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 1200
        self.altura = 600
        self.titulo = 'Investimentos'

        self.lista_investimentos = QListWidget(self)

        self.lista_investimentos.setGeometry(10, 60, self.largura - 20, self.altura - 70)

        self.criar_investimento = QPushButton('Criar Investimento', self)
        self.criar_investimento.move(self.largura - 170, 10)
        self.criar_investimento.resize(170, 40)
        self.criar_investimento.setStyleSheet('QPushButton {background-color: #20C12B}')
        self.criar_investimento.clicked.connect(self.CI_Clicado)

        self.listar_investimento = QPushButton('Listar Investimentos' , self)
        self.listar_investimento.move(self.largura - 340, 10)
        self.listar_investimento.resize(170, 40)
        self.listar_investimento.setStyleSheet('QPushButton {background-color: #17CB6E}')

        self.modificar_investimento = QPushButton('Modificar Investimento', self)
        self.modificar_investimento.move(self.largura - 510, 10)
        self.modificar_investimento.resize(170, 40)
        self.modificar_investimento.setStyleSheet('QPushButton {background-color: #17CBBB}')

        self.deletar_investimento = QPushButton('Deletar Investimento', self)
        self.deletar_investimento.move(self.largura - 680, 10)
        self.deletar_investimento.resize(170, 40)
        self.deletar_investimento.setStyleSheet('QPushButton {background-color: #17ADCB}')
        self.deletar_investimento.clicked.connect(self.DI_Clicado)

        self.salvar_investimentos = QPushButton('Salvar Investimentos', self)
        self.salvar_investimentos.move(self.largura - 850, 10)
        self.salvar_investimentos.resize(170, 40)
        self.salvar_investimentos.setStyleSheet('QPushButton {background-color: #175ECB}')

        self.detalhar_ativo = QPushButton('Detalhar Ativo', self)
        self.detalhar_ativo.move(self.largura - 1020, 10)
        self.detalhar_ativo.resize(170, 40)
        self.detalhar_ativo.setStyleSheet('QPushButton {background-color: #3217CB}')

        self.enviar_dados = QPushButton('Criar', self)
        self.enviar_dados.resize(0, 0)
        self.enviar_dados.setStyleSheet('QPushButton {background-color: #CB177F}')

        self.listar_investimento.clicked.connect(self.LI_Clicado)
        self.modificar_investimento.clicked.connect(self.MI_Clicado)
        self.salvar_investimentos.clicked.connect(self.SI_Clicado)
        self.detalhar_ativo.clicked.connect(self.DA_Clicado)
        self.enviar_dados.clicked.connect(self.Criar_Clicado)

        self.codigo = QLineEdit(self)
        self.codigo.resize(0, 0)
        self.data = QLineEdit(self)
        self.data.resize(0, 0)
        self.quantidade = QLineEdit(self)
        self.quantidade.resize(0, 0)
        self.valor_unidade = QLineEdit(self)
        self.valor_unidade.resize(0, 0)
        self.tipo = QComboBox(self)
        self.tipo.resize(0, 0)
        self.taxa_de_corretagem = QLineEdit(self)
        self.taxa_de_corretagem.resize(0, 0)

        self.tipo.addItems(['Compra', 'Venda'])

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def CI_Clicado(self):
        self.lista_investimentos.setGeometry(10, 120, self.largura - 20, self.altura - 130)
        self.codigo.move(10, 90)
        self.codigo.resize(100, 20)
        self.data.move(120, 90)
        self.data.resize(100, 20)
        self.quantidade.move(230, 90)
        self.quantidade.resize(100, 20)
        self.valor_unidade.move(340, 90)
        self.valor_unidade.resize(100, 20)
        self.tipo.move(450, 90)
        self.tipo.resize(100, 20)
        self.taxa_de_corretagem.move(560, 90)
        self.taxa_de_corretagem.resize(100, 20)
        self.enviar_dados.move(670, 90)
        self.enviar_dados.resize(30, 20)

    def LI_Clicado(self):
        print('Investimentos listados!')

    def MI_Clicado(self):
        print('Investimento modificado!')

    def DI_Clicado(self):
        item_selecionado = self.lista_investimentos.currentRow()
        self.lista_investimentos.takeItem(item_selecionado)

    def SI_Clicado(self):
        print('Investimentos salvos!')

    def DA_Clicado(self):
        print('Ativos detalhados!')

    def Criar_Clicado(self):
        codigo = self.codigo.text()
        data = self.data.text()
        quantidade = self.quantidade.text()
        valor_unidade = self.valor_unidade.text()
        tipo = self.tipo.currentText()
        taxa_de_corretagem = self.taxa_de_corretagem.text()

        if len(codigo) > 5 or len(codigo) < 5:
            self.Mensagem_de_Erro('codigo')
        elif int(quantidade) <= 0:
            self.Mensagem_de_Erro('quantidade')
        elif float(valor_unidade) <= 0:
            self.Mensagem_de_Erro('valor da unidade')
        elif float(taxa_de_corretagem) <= 0:
            self.Mensagem_de_Erro('taxa de corretagem')
        else:
            investimento_atual = Investimento(data, codigo, int(quantidade), float(valor_unidade), tipo, float(taxa_de_corretagem))
            self.lista_investimentos.addItem(investimento_atual.__str__())


    def Mensagem_de_Erro(self, campo):
        QMessageBox.about(self, 'Valor Inválido!', f'O campo "{campo}" foi preenchido errado!')

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec()) 
