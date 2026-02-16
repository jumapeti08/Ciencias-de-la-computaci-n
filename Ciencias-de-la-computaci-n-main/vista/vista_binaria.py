from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from controlador.controlador_binaria import ControladorBusquedaBinaria


class VistaBusquedaBinaria(QWidget):
    def __init__(self, anterior):
        super().__init__()
        self.anterior = anterior
        self.showMaximized()

        layout = QVBoxLayout(self)

        # ===== BOTÓN VOLVER (ARRIBA) =====
        self.btn_volver = QPushButton("⬅ Volver")
        self.btn_volver.setFixedWidth(120)
        self.btn_volver.setStyleSheet("""
            QPushButton{
                background:#588157;
                color:white;
                padding:8px;
                font-size:14px;
            }
            QPushButton:hover{
                background:#6a994e;
            }
        """)
        self.btn_volver.clicked.connect(self.volver)

        layout.addWidget(self.btn_volver, alignment=Qt.AlignLeft)

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
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.verticalHeader().setVisible(False)
        layout.addWidget(self.tabla)

        # ===== SALIDA =====
        self.salida = QTextEdit()
        self.salida.setReadOnly(True)
        layout.addWidget(self.salida)

        # 👉 CONTROLADOR AL FINAL
        self.controlador = ControladorBusquedaBinaria(self)

    # ===== MÉTODOS AUXILIARES =====
    def pedir_valor(self, titulo):
        return QInputDialog.getText(self, titulo, "Ingrese la clave:")

    def item(self, texto):
        i = QTableWidgetItem(texto)
        i.setTextAlignment(Qt.AlignCenter)
        return i

    # ===== NAVEGACIÓN =====
    def volver(self):
        self.anterior.show()
        self.close()

