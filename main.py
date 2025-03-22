import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Criando uma única instância de QApplication
    window = MainWindow()  # Criando a janela principal
    
    label1 = QLabel("O meu texto")
    label1.setStyleSheet("font-size: 50px")
    window.v_layout.addWidget(label1)
    window.adjustFixedSize()
    
    window.show()
    sys.exit(app.exec())  # Executando o loop da aplicação
