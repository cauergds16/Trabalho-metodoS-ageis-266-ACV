import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from investimento import Investimento

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500
        self.titulo = 'Investimentos'

        self.criar_investimento = QPushButton('Criar Investimento', self)
        self.criar_investimento.move(int(self.largura / 100 * 1), int(self.altura / 100 * 1))
        self.criar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
        self.criar_investimento.setStyleSheet('QPushButton {background-color: #20C12B}')
        self.criar_investimento.clicked.connect(self.CI_Clicado)

        self.lista_investimentos = QListWidget(self)
        self.lista_investimentos.setGeometry(int((self.largura / 100 * 1)), int(self.criar_investimento.x() / 100 * 1300), 0, 0)

        self.listar_investimento = QPushButton('Listar Investimentos' , self)
        self.listar_investimento.move(int(self.largura / 100 * 17), int(self.altura / 100 * 1))
        self.listar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
        self.listar_investimento.setStyleSheet('QPushButton {background-color: #17CB6E}')

        self.modificar_investimento = QPushButton('Modificar Investimento', self)
        self.modificar_investimento.move(int(self.largura / 100 * 33), int(self.altura / 100 * 1))
        self.modificar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
        self.modificar_investimento.setStyleSheet('QPushButton {background-color: #17CBBB}')

        self.deletar_investimento = QPushButton('Deletar Investimento', self)
        self.deletar_investimento.move(int(self.largura / 100 * 52), int(self.altura / 100 * 1))
        self.deletar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
        self.deletar_investimento.setStyleSheet('QPushButton {background-color: #17ADCB}')
        self.deletar_investimento.clicked.connect(self.DI_Clicado)

        self.salvar_investimentos = QPushButton('Salvar Investimentos', self)
        self.salvar_investimentos.move(int(self.largura / 100 * 68), int(self.altura / 100 * 1))
        self.salvar_investimentos.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
        self.salvar_investimentos.setStyleSheet('QPushButton {background-color: #175ECB}')

        self.detalhar_ativo = QPushButton('Detalhar Ativo', self)
        self.detalhar_ativo.move(int(self.largura / 100 * 84), int(self.altura / 100 * 1))
        self.detalhar_ativo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
        self.detalhar_ativo.setStyleSheet('QPushButton {background-color: #3217CB}')

        self.enviar_dados = QPushButton('Criar', self)
        self.enviar_dados.move(int((self.largura / 100 * 91)), int(self.criar_investimento.x() / 100 * 800))
        self.enviar_dados.resize(0, 0)
        self.enviar_dados.setStyleSheet('QPushButton {background-color: #CB177F}')

        self.listar_investimento.clicked.connect(self.LI_Clicado)
        self.modificar_investimento.clicked.connect(self.MI_Clicado)
        self.salvar_investimentos.clicked.connect(self.SI_Clicado)
        self.detalhar_ativo.clicked.connect(self.DA_Clicado)
        self.enviar_dados.clicked.connect(self.Criar_Clicado)

        # Criar Investimento:
        self.codigo = QLineEdit(self)
        self.codigo.resize(0, 0)
        self.codigo.move(int((self.largura / 100 * 1)), int(self.criar_investimento.x() / 100 * 800))
        self.data = QLineEdit(self)
        self.data.resize(0, 0)
        self.data.move(int((self.largura / 100 * 16)), int(self.criar_investimento.x() / 100 * 800))
        self.quantidade = QLineEdit(self)
        self.quantidade.resize(0, 0)
        self.quantidade.move(int((self.largura / 100 * 31)), int(self.criar_investimento.x() / 100 * 800))
        self.valor_unidade = QLineEdit(self)
        self.valor_unidade.resize(0, 0)
        self.valor_unidade.move(int((self.largura / 100 * 46)), int(self.criar_investimento.x() / 100 * 800))
        self.tipo = QComboBox(self)
        self.tipo.resize(0, 0)
        self.tipo.addItems(['Compra', 'Venda'])
        self.tipo.move(int((self.largura / 100 * 61)), int(self.criar_investimento.x() / 100 * 800))
        self.taxa_de_corretagem = QLineEdit(self)
        self.taxa_de_corretagem.resize(0, 0)
        self.taxa_de_corretagem.move(int((self.largura / 100 * 76)), int(self.criar_investimento.x() / 100 * 800))


        self.CarregarJanela()

    def MudarTamanho(self):
        if self.largura == 800:
            self.largura = self.width()
            self.altura = self.height()

            self.criar_investimento.move(int(self.largura / 100 * 1), int(self.altura / 100 * 1))
            self.criar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.listar_investimento.move(int(self.largura / 100 * 17), int(self.altura / 100 * 1))
            self.listar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.modificar_investimento.move(int(self.largura / 100 * 33), int(self.altura / 100 * 1))
            self.modificar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.deletar_investimento.move(int(self.largura / 100 * 52), int(self.altura / 100 * 1))
            self.deletar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.deletar_investimento.clicked.connect(self.DI_Clicado)
            self.salvar_investimentos.move(int(self.largura / 100 * 68), int(self.altura / 100 * 1))
            self.salvar_investimentos.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.detalhar_ativo.move(int(self.largura / 100 * 84), int(self.altura / 100 * 1))
            self.detalhar_ativo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))

            if self.codigo.height() != 0:

                self.lista_investimentos.resize(int((self.largura / 100 * 98)), int((self.altura / 100 * 78)))
                self.lista_investimentos.move(int((self.largura / 100 * 1)), int(self.criar_investimento.x() / 100 * 1300))

                self.codigo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.codigo.move(int((self.largura / 100 * 1)), int(self.criar_investimento.x() / 100 * 800))
                self.data.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.data.move(int((self.largura / 100 * 16)), int(self.criar_investimento.x() / 100 * 800))
                self.quantidade.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.quantidade.move(int((self.largura / 100 * 31)), int(self.criar_investimento.x() / 100 * 800))                   
                self.valor_unidade.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.valor_unidade.move(int((self.largura / 100 * 46)), int(self.criar_investimento.x() / 100 * 800))
                self.tipo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.tipo.move(int((self.largura / 100 * 61)), int(self.criar_investimento.x() / 100 * 800))
                self.taxa_de_corretagem.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.taxa_de_corretagem.move(int((self.largura / 100 * 76)), int(self.criar_investimento.x() / 100 * 800))
                self.enviar_dados.move(int((self.largura / 100 * 91)), int(self.criar_investimento.x() / 100 * 800))
                self.enviar_dados.resize(int((self.largura / 100 * 8)), int((self.altura / 100 * 3)))

        else:
            self.largura = 800
            self.altura = 500

            self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)

            self.criar_investimento.move(int(self.largura / 100 * 1), int(self.altura / 100 * 1))
            self.criar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.listar_investimento.move(int(self.largura / 100 * 17), int(self.altura / 100 * 1))
            self.listar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.modificar_investimento.move(int(self.largura / 100 * 33), int(self.altura / 100 * 1))
            self.modificar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.deletar_investimento.move(int(self.largura / 100 * 52), int(self.altura / 100 * 1))
            self.deletar_investimento.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.deletar_investimento.clicked.connect(self.DI_Clicado)
            self.salvar_investimentos.move(int(self.largura / 100 * 68), int(self.altura / 100 * 1))
            self.salvar_investimentos.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))
            self.detalhar_ativo.move(int(self.largura / 100 * 84), int(self.altura / 100 * 1))
            self.detalhar_ativo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 6)))

            if self.codigo.height() != 0:

                self.lista_investimentos.resize(int((self.largura / 100 * 98)), int((self.altura / 100 * 78)))
                self.lista_investimentos.move(int((self.largura / 100 * 1)), int(self.criar_investimento.x() / 100 * 1300))

                self.codigo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.codigo.move(int((self.largura / 100 * 1)), int(self.criar_investimento.x() / 100 * 800))
                self.data.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.data.move(int((self.largura / 100 * 16)), int(self.criar_investimento.x() / 100 * 800))
                self.quantidade.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.quantidade.move(int((self.largura / 100 * 31)), int(self.criar_investimento.x() / 100 * 800))                   
                self.valor_unidade.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.valor_unidade.move(int((self.largura / 100 * 46)), int(self.criar_investimento.x() / 100 * 800))
                self.tipo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.tipo.move(int((self.largura / 100 * 61)), int(self.criar_investimento.x() / 100 * 800))
                self.taxa_de_corretagem.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
                self.taxa_de_corretagem.move(int((self.largura / 100 * 76)), int(self.criar_investimento.x() / 100 * 800))
                self.enviar_dados.move(int((self.largura / 100 * 91)), int(self.criar_investimento.x() / 100 * 800))
                self.enviar_dados.resize(int((self.largura / 100 * 8)), int((self.altura / 100 * 3)))

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def CI_Clicado(self):
        if self.codigo.height() == 0:

            self.lista_investimentos.resize(int((self.largura / 100 * 98)), int((self.altura / 100 * 78)))

            self.codigo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
            self.data.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
            self.quantidade.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
            self.valor_unidade.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
            self.tipo.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
            self.taxa_de_corretagem.resize(int((self.largura / 100 * 15)), int((self.altura / 100 * 3)))
            self.enviar_dados.resize(int((self.largura / 100 * 8)), int((self.altura / 100 * 3)))

        else:

            self.lista_investimentos.resize(0, 0)

            self.codigo.resize(0, 0)
            self.data.resize(0, 0)
            self.quantidade.resize(0, 0)
            self.valor_unidade.resize(0, 0)
            self.tipo.resize(0, 0)
            self.taxa_de_corretagem.resize(0, 0)
            self.enviar_dados.resize(0, 0)

    def LI_Clicado(self):
        if self.lista_investimentos.height() == 0: 
            self.lista_investimentos.resize(int((self.largura / 100 * 98)), int((self.altura / 100 * 78)))
        else:
            self.lista_investimentos.resize(0, 0)

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

    def changeEvent(self, event):
        if event.type() == event.WindowStateChange:
            if self.isMaximized():
                self.MudarTamanho()
            else:
                self.MudarTamanho()             
               
            
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec()) 