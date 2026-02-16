from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout,
    QPushButton, QFrame
)
from PySide6.QtCore import Qt


from .interfaz_internas import InterfazInternas
from .interfaz_externas import InterfazExternas
from .interfaz_indices import InterfazIndices


class VentanaBusquedas(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        layout = QHBoxLayout(self)

        # ===== SIDEBAR =====
        sidebar = QFrame()
        sidebar.setFixedWidth(330)
        sidebar.setStyleSheet("background-color: #2f3e46;")
        s_layout = QVBoxLayout(sidebar)

        titulo = QLabel("BÚSQUEDAS")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet(
            "color:white;font-size:22px;font-weight:bold;padding:20px;"
        )
        s_layout.addWidget(titulo)

        btn_internas = self.boton("📁 Internas")
        btn_externas = self.boton("🌐 Externas")
        btn_indices = self.boton("📌 Índices")
        btn_volver = self.boton("⬅ Volver")

        btn_internas.clicked.connect(self.abrir_internas)
        btn_externas.clicked.connect(self.abrir_externas)
        btn_indices.clicked.connect(self.abrir_indices)
        btn_volver.clicked.connect(self.volver_inicio)

        s_layout.addWidget(btn_internas)
        s_layout.addWidget(btn_externas)
        s_layout.addWidget(btn_indices)
        s_layout.addSpacing(20)
        s_layout.addWidget(btn_volver)
        s_layout.addStretch()

        # ===== CONTENIDO =====
        contenido = QFrame()
        contenido.setStyleSheet("background-color:#edf6f9;")
        c_layout = QVBoxLayout(contenido)

        label = QLabel("Seleccione un tipo de búsqueda")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size:26px;color:#2f3e46;")

        c_layout.addStretch()
        c_layout.addWidget(label)
        c_layout.addStretch()

        layout.addWidget(sidebar)
        layout.addWidget(contenido)

    def boton(self, texto):
        btn = QPushButton(texto)
        btn.setStyleSheet("""
            QPushButton{
                background-color:#354f52;
                color:white;
                padding:14px;
                text-align:left;
                border:none;
                font-size:15px;
            }
            QPushButton:hover{
                background-color:#52796f;
            }
        """)
        return btn

    def abrir_internas(self):
        self.i = InterfazInternas(self)
        self.i.show()
        self.close()

    def abrir_externas(self):
        self.e = InterfazExternas(self)
        self.e.show()
        self.close()

    def abrir_indices(self):
        self.ind = InterfazIndices(self)
        self.ind.show()
        self.close()

    def volver_inicio(self):
        from pantalla_inicio import PantallaInicio
        self.inicio = PantallaInicio()
        self.inicio.show()
        self.close()
