import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PySide6.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciencia de la Computación 2")
        self.setFixedSize(500, 600)

        # Fondo
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f3f1;
                font-family: Arial;
            }
        """)

        # Título
        titulo = QLabel("Ciencia de la\nComputación 2")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #2c3e50;
            }
        """)

        # Botón Búsquedas
        btn_busquedas = QPushButton("Búsquedas")
        btn_busquedas.setFixedHeight(90)
        btn_busquedas.setStyleSheet("""
            QPushButton {
                background-color: #ff8f7a;
                border-radius: 30px;
                font-size: 24px;
                color: #2c3e50;
            }
            QPushButton:hover {
                background-color: #ff7a61;
            }
        """)

        # Botón Grafos
        btn_grafos = QPushButton("Grafos")
        btn_grafos.setFixedHeight(90)
        btn_grafos.setStyleSheet("""
            QPushButton {
                background-color: #63c7c2;
                border-radius: 30px;
                font-size: 24px;
                color: #2c3e50;
            }
            QPushButton:hover {
                background-color: #52b5b0;
            }
        """)

        # Layout
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(titulo)
        layout.addSpacing(50)
        layout.addWidget(btn_busquedas)
        layout.addSpacing(30)
        layout.addWidget(btn_grafos)
        layout.addStretch()

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
