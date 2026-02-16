from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QPushButton, QFrame
)
from PySide6.QtCore import Qt
from vista.ventana_busquedas import VentanaBusquedas
# from vista.ventana_grafos import VentanaGrafos  # Descomenta cuando la tengas


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

        subtitulo = QLabel("Seleccione una opción")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setStyleSheet("""
            font-size: 20px;
            color: #344e41;
        """)

        # -------- BOTÓN BÚSQUEDAS --------
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

        # -------- BOTÓN GRAFOS --------
        btn_grafos = QPushButton("GRAFOS")
        btn_grafos.setFixedSize(280, 80)
        btn_grafos.setStyleSheet("""
            QPushButton {
                background-color: #6a4c93;
                color: white;
                font-size: 22px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #8a5fbf;
            }
        """)
        btn_grafos.clicked.connect(self.abrir_grafos)

        cont_layout.addStretch()
        cont_layout.addWidget(titulo)
        cont_layout.addSpacing(30)
        cont_layout.addWidget(subtitulo)
        cont_layout.addSpacing(40)
        cont_layout.addWidget(btn_busquedas, alignment=Qt.AlignCenter)
        cont_layout.addSpacing(20)
        cont_layout.addWidget(btn_grafos, alignment=Qt.AlignCenter)
        cont_layout.addStretch()

        layout.addWidget(contenedor)

    def abrir_busquedas(self):
        self.busquedas = VentanaBusquedas()
        self.busquedas.show()
        self.close()

    def abrir_grafos(self):
        print("Abrir ventana de grafos")
        # self.grafos = VentanaGrafos()
        # self.grafos.show()
        # self.close()

