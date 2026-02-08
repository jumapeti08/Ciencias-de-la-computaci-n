import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QFrame
)
from PySide6.QtCore import Qt


class MenuButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setCheckable(True)
        self.setStyleSheet("""
            QPushButton {
                background-color: #354f52;
                color: white;
                border: none;
                padding: 12px;
                text-align: left;
                font-size: 14px;
            }
            QPushButton:hover, QPushButton:checked {
                background-color: #52796f;
            }
        """)


class SubButton(QPushButton):
    def __init__(self, text, indent=25):
        super().__init__(text)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: #3a5a60;
                color: white;
                border: none;
                padding: 8px;
                padding-left: {indent}px;
                text-align: left;
                font-size: 13px;
            }}
            QPushButton:hover {{
                background-color: #588157;
            }}
        """)


class VentanaBusquedas(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        layout_principal = QHBoxLayout(self)

        # ===== SIDEBAR =====
        sidebar = QFrame()
        sidebar.setFixedWidth(330)
        sidebar.setStyleSheet("background-color: #2f3e46;")
        sidebar_layout = QVBoxLayout(sidebar)

        titulo = QLabel("BÚSQUEDAS")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 22px;
                font-weight: bold;
                padding: 15px;
            }
        """)
        sidebar_layout.addWidget(titulo)

        # ===== INTERNAS =====
        internas_btn = MenuButton("📁 Internas")
        internas_menu = QFrame()
        internas_layout = QVBoxLayout(internas_menu)

        internas_layout.addWidget(SubButton("Secuencial"))
        internas_layout.addWidget(SubButton("Binaria"))
        internas_layout.addWidget(SubButton("Por transformación de claves"))

        # --- Árbol (dentro de Internas) ---
        arbol_btn = MenuButton("Árbol")

        arbol_menu = QFrame()
        arbol_menu.setStyleSheet("background-color: #3a5a60;")
        arbol_layout = QVBoxLayout(arbol_menu)
        arbol_layout.setContentsMargins(0, 0, 0, 0)
        arbol_layout.setSpacing(0)

        arbol_layout.addWidget(SubButton("Búsquedas por residuos", 45))
        arbol_layout.addWidget(SubButton("Árboles de búsqueda digital", 45))
        arbol_layout.addWidget(SubButton("Por residuos múltiple", 45))
        arbol_layout.addWidget(SubButton("Tablas de índices", 45))

        # ---- Métodos elementales ----
        metodos_btn = MenuButton("Métodos elementales")

        metodos_menu = QFrame()
        metodos_menu.setStyleSheet("background-color: #3a5a60;")
        metodos_layout = QVBoxLayout(metodos_menu)
        metodos_layout.setContentsMargins(0, 0, 0, 0)
        metodos_layout.setSpacing(0)

        metodos_layout.addWidget(SubButton("Método de la rejilla", 65))
        metodos_layout.addWidget(SubButton("Árboles 2D", 65))

        metodos_menu.setVisible(False)
        metodos_btn.clicked.connect(
            lambda: metodos_menu.setVisible(not metodos_menu.isVisible())
        )

        arbol_layout.addWidget(metodos_btn)
        arbol_layout.addWidget(metodos_menu)

        arbol_menu.setVisible(False)
        arbol_btn.clicked.connect(
            lambda: arbol_menu.setVisible(not arbol_menu.isVisible())
        )



        internas_layout.addWidget(arbol_btn)
        internas_layout.addWidget(arbol_menu)

        internas_menu.setVisible(False)
        internas_btn.clicked.connect(
            lambda: internas_menu.setVisible(not internas_menu.isVisible())
        )

        # ===== EXTERNAS =====
        externas_btn = MenuButton("🌐 Externas")
        externas_menu = QFrame()
        externas_layout = QVBoxLayout(externas_menu)

        hash_btn = MenuButton("Funciones hash o de dispersión")
        botonBinaria = MenuButton("Binaria")
        botonSecuencial = MenuButton("Secuencial")
        botonTransformacion = MenuButton("Por transformación de claves")
        hash_menu = QFrame()
        hash_layout = QVBoxLayout(hash_menu)

        hash_layout.addWidget(SubButton("Módulo", 45))
        hash_layout.addWidget(SubButton("Cuadrado", 45))
        hash_layout.addWidget(SubButton("Truncamiento", 45))
        hash_layout.addWidget(SubButton("Conversión de bases", 45))

        hash_menu.setVisible(False)
        hash_btn.clicked.connect(
            lambda: hash_menu.setVisible(not hash_menu.isVisible())
        )

        externas_layout.addWidget(hash_btn)
        externas_layout.addWidget(botonBinaria)
        externas_layout.addWidget(botonSecuencial)
        externas_layout.addWidget(botonTransformacion)
        externas_layout.addWidget(hash_menu)

        externas_menu.setVisible(False)
        externas_btn.clicked.connect(
            lambda: externas_menu.setVisible(not externas_menu.isVisible())
        )

        # ===== ÍNDICES =====
        indices_btn = MenuButton("📌 Índices")

        # ===== AGREGAR A SIDEBAR =====
        sidebar_layout.addWidget(internas_btn)
        sidebar_layout.addWidget(internas_menu)
        sidebar_layout.addSpacing(8)

        sidebar_layout.addWidget(externas_btn)
        sidebar_layout.addWidget(externas_menu)
        sidebar_layout.addSpacing(8)

        sidebar_layout.addWidget(indices_btn)
        sidebar_layout.addStretch()

        # ===== CONTENIDO =====
        contenido = QFrame()
        contenido.setStyleSheet("background-color: #edf6f9;")
        contenido_layout = QVBoxLayout(contenido)

        label = QLabel("Seleccione un procedimiento")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            font-size: 26px;
            color: #2f3e46;
        """)

        contenido_layout.addStretch()
        contenido_layout.addWidget(label)
        contenido_layout.addStretch()

        layout_principal.addWidget(sidebar)
        layout_principal.addWidget(contenido)


