import sys
from PySide6.QtWidgets import QApplication
from vista.pantalla_inicio import PantallaInicio


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inicio = PantallaInicio()
    inicio.show()
    sys.exit(app.exec())
