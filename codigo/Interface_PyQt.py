import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit, QVBoxLayout, QListWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 1200
        self.altura = 600
        self.titulo = 'Investimentos'

        lista_investimentos = QListWidget(self)

        lista_investimentos.setGeometry(10, 60, self.largura - 20, self.altura - 70)

        self.criar_investimento = QPushButton('Criar Investimento', self)
        self.criar_investimento.move(self.largura - 170, 10)
        self.criar_investimento.resize(170, 40)
        self.criar_investimento.setStyleSheet('QPushButton {background-color: #20C12B}')

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

        self.salvar_investimentos = QPushButton('Salvar Investimentos', self)
        self.salvar_investimentos.move(self.largura - 850, 10)
        self.salvar_investimentos.resize(170, 40)
        self.salvar_investimentos.setStyleSheet('QPushButton {background-color: #175ECB}')

        self.detalhar_ativo = QPushButton('Detalhar Ativo', self)
        self.detalhar_ativo.move(self.largura - 1020, 10)
        self.detalhar_ativo.resize(170, 40)
        self.detalhar_ativo.setStyleSheet('QPushButton {background-color: #3217CB}')

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec())