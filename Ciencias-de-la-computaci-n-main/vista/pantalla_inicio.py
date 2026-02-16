from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QPushButton, QFrame
)
from PySide6.QtCore import Qt
from vista.ventana_busquedas import VentanaBusquedas


class PantallaInicio(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        layout = QVBoxLayout(self)

        contenedor = QFrame()
        contenedor.setStyleSheet("background-color:#edf6f9;")
        cont_layout = QVBoxLayout(contenedor)

        titulo = QLabel("Ciencias de la Computación II")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color: #2f3e46;
        """)

        btn_busquedas = QPushButton("BÚSQUEDAS")
        btn_busquedas.setFixedSize(280, 80)
        btn_busquedas.setStyleSheet("""
            QPushButton {
                background-color: #354f52;
                color: white;
                font-size: 22px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #52796f;
            }
        """)
        btn_busquedas.clicked.connect(self.abrir_busquedas)

        cont_layout.addStretch()
        cont_layout.addWidget(titulo)
        cont_layout.addSpacing(50)
        cont_layout.addWidget(btn_busquedas, alignment=Qt.AlignCenter)
        cont_layout.addStretch()

        layout.addWidget(contenedor)

    def abrir_busquedas(self):
        self.busquedas = VentanaBusquedas()
        self.busquedas.show()
        self.close()
