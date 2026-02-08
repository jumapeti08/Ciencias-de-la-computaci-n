import sys
from PySide6.QtWidgets import QApplication
from busquedas_view import VentanaBusquedas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaBusquedas()
    ventana.show()
    sys.exit(app.exec())

