import sys
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet("font-size: 150px")
    return label1


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Criando uma única instância de QApplication
    window = MainWindow()  # Criando a janela principal
    window.addWidgetToVLayout(temp_label("Label 1"))
    
    # Define o Icone do app
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    
    #Executa Tudo
    window.adjustFixedSize()
    window.show()
    sys.exit(app.exec())  # Executando o loop da aplicação
