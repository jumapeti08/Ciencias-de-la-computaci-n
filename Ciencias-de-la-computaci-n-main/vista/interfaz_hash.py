from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class InterfazHash(QWidget):
    def __init__(self, anterior):
        super().__init__()
        self.anterior = anterior
        self.showMaximized()

        layout = QHBoxLayout(self)

        sidebar = QFrame()
        sidebar.setFixedWidth(330)
        sidebar.setStyleSheet("background:#2f3e46;")
        s = QVBoxLayout(sidebar)

        titulo = QLabel("FUNCIONES HASH")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:white;font-size:20px;padding:15px;")
        s.addWidget(titulo)

        opciones = [
            "Función módulo",
            "Función cuadrado",
            "Función truncamiento",
            "Función plegamiento"
        ]

        for op in opciones:
            s.addWidget(self.boton(op))

        s.addStretch()
        s.addWidget(self.volver())

        contenido = self.contenido("Seleccione una función hash")

        layout.addWidget(sidebar)
        layout.addWidget(contenido)

    def boton(self, t):
        b = QPushButton(t)
        b.setStyleSheet("""
            QPushButton{background:#354f52;color:white;padding:12px;text-align:left;border:none;}
            QPushButton:hover{background:#52796f;}
        """)
        return b

    def volver(self):
        b = QPushButton("⬅ Volver")
        b.setStyleSheet("background:#588157;color:white;padding:12px;")
        b.clicked.connect(self.regresar)
        return b

    def regresar(self):
        self.anterior.show()
        self.close()

    def contenido(self, t):
        c = QFrame()
        c.setStyleSheet("background:#edf6f9;")
        l = QVBoxLayout(c)
        lbl = QLabel(t)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("font-size:24px;color:#2f3e46;")
        l.addStretch()
        l.addWidget(lbl)
        l.addStretch()
        return c
