from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

from .vista_lineal import VistaBusquedaLineal
from .vista_binaria import VistaBusquedaBinaria
from .interfaz_hash import InterfazHash
from .interfaz_arboles import InterfazArboles


class InterfazInternas(QWidget):
    def __init__(self, anterior):
        super().__init__()
        self.anterior = anterior
        self.showMaximized()

        layout = QHBoxLayout(self)

        # ---------- SIDEBAR ----------
        sidebar = QFrame()
        sidebar.setFixedWidth(330)
        sidebar.setStyleSheet("background-color:#2f3e46;")
        s = QVBoxLayout(sidebar)

        titulo = QLabel("CIENCIAS DE LA COMPUTACIÓN 2")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color:white;
            font-size:20px;
            font-weight:bold;
            padding:15px;
        """)
        s.addWidget(titulo)

        # ---------- BOTONES ----------
        btn_secuencial = self.boton("Secuencial")
        btn_binaria = self.boton("Binaria")
        btn_hash = self.boton("Funciones Hash")
        btn_arboles = self.boton("Árboles de búsqueda")

        # ---------- CONEXIONES ----------
        btn_secuencial.clicked.connect(self.abrir_secuencial)
        btn_binaria.clicked.connect(self.abrir_binaria)
        btn_hash.clicked.connect(self.abrir_hash)
        btn_arboles.clicked.connect(self.abrir_arboles)

        for b in [btn_secuencial, btn_binaria, btn_hash, btn_arboles]:
            s.addWidget(b)

        s.addStretch()
        s.addWidget(self.boton_volver())

        # ---------- CONTENIDO ----------
        self.contenido = QFrame()
        self.contenido.setStyleSheet("background:#edf6f9;")
        c = QVBoxLayout(self.contenido)

        label = QLabel("Seleccione un algoritmo de búsqueda interna")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            font-size:24px;
            color:#2f3e46;
        """)

        c.addStretch()
        c.addWidget(label)
        c.addStretch()

        layout.addWidget(sidebar)
        layout.addWidget(self.contenido)

    # ---------- COMPONENTES ----------
    def boton(self, texto):
        b = QPushButton(texto)
        b.setStyleSheet("""
            QPushButton{
                background:#354f52;
                color:white;
                padding:14px;
                text-align:left;
                border:none;
                font-size:15px;
            }
            QPushButton:hover{
                background:#52796f;
            }
        """)
        return b

    def boton_volver(self):
        b = QPushButton("⬅ Volver")
        b.setStyleSheet("""
            QPushButton{
                background:#588157;
                color:white;
                padding:12px;
                font-size:14px;
            }
            QPushButton:hover{
                background:#6a994e;
            }
        """)
        b.clicked.connect(self.regresar)
        return b

    # ---------- NAVEGACIÓN ----------
    def regresar(self):
        self.anterior.show()
        self.close()

    def abrir_secuencial(self):
        self.v = VistaBusquedaLineal(self)
        self.v.show()
        self.close()

    def abrir_binaria(self):
        self.b = VistaBusquedaBinaria(self)
        self.b.show()
        self.close()

    def abrir_hash(self):
        self.h = InterfazHash(self)
        self.h.show()
        self.close()

    def abrir_arboles(self):
        self.a = InterfazArboles(self)
        self.a.show()
        self.close()
