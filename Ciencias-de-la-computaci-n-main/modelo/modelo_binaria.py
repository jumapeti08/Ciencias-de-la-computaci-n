class ModeloBusquedaBinaria:
    def __init__(self):
        self.datos = []
        self.maximo = 0

    def crear(self, n):
        self.maximo = n
        self.datos = []

    def insertar(self, valor):
        if valor in self.datos:
            return False
        self.datos.append(valor)
        self.datos.sort()
        return True

    def buscar(self, valor):
        low, high = 0, len(self.datos) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.datos[mid] == valor:
                return mid
            elif valor < self.datos[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def eliminar(self, valor):
        if valor in self.datos:
            self.datos.remove(valor)
            return True
        return False
