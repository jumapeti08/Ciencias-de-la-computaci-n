from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from controlador.controlador_lineal import ControladorBusquedaLineal


class VistaBusquedaLineal(QWidget):
    def __init__(self, anterior):
        super().__init__()
        self.anterior = anterior
        self.showMaximized()

        layout = QVBoxLayout(self)

        # === PARTE SUPERIOR ===
        top = QHBoxLayout()
        self.input_rango = QLineEdit()
        self.input_rango.setFixedWidth(80)

        self.spin_digitos = QSpinBox()
        self.spin_digitos.setRange(1, 10)

        top.addWidget(QLabel("Cantidad:"))
        top.addWidget(self.input_rango)
        top.addWidget(QLabel("Dígitos:"))
        top.addWidget(self.spin_digitos)
        top.addStretch()
        layout.addLayout(top)

        # === BOTONES ===
        self.btn_crear = QPushButton("Crear estructura")
        self.btn_insertar = QPushButton("Insertar")
        self.btn_buscar = QPushButton("Buscar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_deshacer = QPushButton("Deshacer")

        grid = QGridLayout()
        for i, b in enumerate([
            self.btn_crear, self.btn_insertar,
            self.btn_buscar, self.btn_eliminar,
            self.btn_deshacer
        ]):
            grid.addWidget(b, i // 3, i % 3)

        layout.addLayout(grid)

        # === TABLA ===
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(["Claves"])
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        layout.addWidget(self.tabla)

        # === SALIDA ===
        self.salida = QTextEdit()
        self.salida.setReadOnly(True)
        layout.addWidget(self.salida)

        self.controlador = ControladorBusquedaLineal(self)

    # ===== MÉTODOS VISUALES =====
    def crear_tabla(self, filas):
        self.tabla.setRowCount(filas)
        for i in range(filas):
            self.tabla.setItem(i, 0, QTableWidgetItem(""))

    def actualizar_tabla(self, datos):
        self.tabla.clearContents()
        for i, val in enumerate(datos):
            self.tabla.setItem(i, 0, QTableWidgetItem(val))

    def resaltar_fila(self, fila):
        self.tabla.selectRow(fila)

    def mensaje(self, texto):
        self.salida.append(texto)
