from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from controlador.controlador_binaria import ControladorBusquedaBinaria


class VistaBusquedaBinaria(QWidget):
    def __init__(self, anterior):
        super().__init__()
        self.anterior = anterior
        self.showMaximized()

        layout = QVBoxLayout(self)

        # ===== PARTE SUPERIOR =====
        top = QHBoxLayout()

        self.input_rango = QLineEdit()
        self.input_rango.setPlaceholderText("Cantidad de datos")

        self.spin_digitos = QSpinBox()
        self.spin_digitos.setRange(1, 10)

        top.addWidget(QLabel("Cantidad de datos:"))
        top.addWidget(self.input_rango)
        top.addSpacing(20)
        top.addWidget(QLabel("Número de dígitos:"))
        top.addWidget(self.spin_digitos)
        top.addStretch()

        layout.addLayout(top)

        # ===== BOTONES =====
        grid = QGridLayout()

        self.btn_crear = QPushButton("Crear estructura")
        self.btn_insertar = QPushButton("Insertar claves")
        self.btn_buscar = QPushButton("Buscar clave")
        self.btn_eliminar = QPushButton("Eliminar clave")

        botones = [
            self.btn_crear, self.btn_insertar,
            self.btn_buscar, self.btn_eliminar
        ]

        for i, b in enumerate(botones):
            grid.addWidget(b, 0, i)

        layout.addLayout(grid)

        # ===== TABLA =====
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(["Claves"])
        layout.addWidget(self.tabla)

        # ===== SALIDA =====
        self.salida = QTextEdit()
        self.salida.setReadOnly(True)
        layout.addWidget(self.salida)

        btn_volver = QPushButton("⬅ Volver")
        btn_volver.clicked.connect(self.volver)
        layout.addWidget(btn_volver)

        # 👉 CONTROLADOR AL FINAL
        self.controlador = ControladorBusquedaBinaria(self)

    def pedir_valor(self, titulo):
        return QInputDialog.getText(self, titulo, "Ingrese la clave:")

    def item(self, texto):
        i = QTableWidgetItem(texto)
        i.setTextAlignment(Qt.AlignCenter)
        return i

    def volver(self):
        self.anterior.show()
        self.close()
