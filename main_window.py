from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Criando o widget central e o layout vertical
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Definindo o título da janela
        self.setWindowTitle('Calculadora')

    # Ajusta o tamanho fixo da janela com base no conteúdo
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adiciona um widget ao layout vertical
    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
