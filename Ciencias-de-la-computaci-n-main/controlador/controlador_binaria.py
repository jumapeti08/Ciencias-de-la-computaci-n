from PySide6.QtWidgets import QMessageBox
from modelo.modelo_binaria import ModeloBusquedaBinaria


class ControladorBusquedaBinaria:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = ModeloBusquedaBinaria()
        self.conectar()

    def conectar(self):
        self.vista.btn_crear.clicked.connect(self.crear)
        self.vista.btn_insertar.clicked.connect(self.insertar)
        self.vista.btn_buscar.clicked.connect(self.buscar)
        self.vista.btn_eliminar.clicked.connect(self.eliminar)

    def crear(self):
        try:
            n = int(self.vista.input_rango.text())
            if n <= 0:
                raise ValueError
        except:
            self.error("El rango debe ser un número entero positivo")
            return

        self.modelo.crear(n)
        self.vista.tabla.setRowCount(n)
        self.vista.salida.setText("Estructura creada")

    def insertar(self):
        digitos = self.vista.spin_digitos.value()

        valor, ok = self.vista.pedir_valor("Insertar clave")
        if not ok:
            return

        if not valor.isdigit() or len(valor) != digitos:
            self.error(f"La clave debe tener exactamente {digitos} dígitos")
            return

        valor = int(valor)

        if not self.modelo.insertar(valor):
            self.error("La clave ya existe")
            return

        self.actualizar_tabla()

    def buscar(self):
        valor, ok = self.vista.pedir_valor("Buscar clave")
        if not ok:
            return

        valor = int(valor)
        pos = self.modelo.buscar(valor)

        if pos == -1:
            self.error("Clave no encontrada")
        else:
            self.vista.tabla.selectRow(pos)
            self.vista.salida.setText(f"Clave encontrada en posición {pos}")

    def eliminar(self):
        valor, ok = self.vista.pedir_valor("Eliminar clave")
        if not ok:
            return

        valor = int(valor)

        if not self.modelo.eliminar(valor):
            self.error("La clave no existe")
            return

        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.vista.tabla.clearContents()
        for i, v in enumerate(self.modelo.datos):
            self.vista.tabla.setItem(i, 0, self.vista.item(str(v)))

    def error(self, msg):
        QMessageBox.critical(self.vista, "Error", msg)
