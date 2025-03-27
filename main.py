import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from display import Display  # Importando a classe Display corretamente
from info import info

# Função temporária para criar um QLabel estilizado
def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet("font-size: 50px")
    return label1

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Criando uma única instância de QApplication
    window = MainWindow()  # Criando a janela principal

    # Define o ícone do aplicativo corretamente (tanto para a janela quanto para a barra de tarefas)
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon)  # Ícone para a barra de tarefas
    window.setWindowIcon(icon)  # Ícone para a janela

    # Info
    info = info("2.0 ^ 10.0 = 1024")
    window.addToVLayout(info)

    # Criando e adicionando o display na interface
    display = Display()
    # display.setPlaceholderText("Digite Algo")
    window.addToVLayout(display)

    # Ajusta o tamanho fixo da janela
    window.adjustFixedSize()
    # Exibe a janela principal
    window.show()
    # Executa o loop da aplicação
    sys.exit(app.exec())  
