from pathlib import Path

# Define o diretório raiz corretamente
ROOT_DIR = Path(__file__).resolve().parent

# Diretório de arquivos
FILES_DIR = ROOT_DIR / "files"

# Caminho do ícone da janela
WINDOW_ICON_PATH = FILES_DIR / "icon.png"

# Definição de tamanhos de fonte
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 450