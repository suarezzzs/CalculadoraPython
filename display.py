from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):  # Corrigido o erro no nome do método
        super().__init__(*args, **kwargs)
        self.configStyle()  # Chamando a função para configurar o estilo

    def configStyle(self):  # Corrigida a indentação
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)  # Definindo altura adequada
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)