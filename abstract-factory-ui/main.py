from abc import ABC, abstractmethod


class Boton(ABC):

    @abstractmethod
    def renderizar(self):
        pass


class Ventana(ABC):

    @abstractmethod
    def abrir(self):
        pass


class BotonWindows(Boton):

    def renderizar(self):
        print("🪟 Botón estilo Windows renderizado para AsereDesk")


class VentanaWindows(Ventana):

    def abrir(self):
        print("🪟 Ventana Windows abierta correctamente")


class BotonMac(Boton):

    def renderizar(self):
        print("🍎 Botón estilo macOS renderizado para AsereDesk")


class VentanaMac(Ventana):

    def abrir(self):
        print("🍎 Ventana macOS abierta correctamente")


class FabricaUI(ABC):

    @abstractmethod
    def crear_boton(self):
        pass

    @abstractmethod
    def crear_ventana(self):
        pass


class FabricaWindows(FabricaUI):

    def crear_boton(self):
        return BotonWindows()

    def crear_ventana(self):
        return VentanaWindows()


class FabricaMac(FabricaUI):

    def crear_boton(self):
        return BotonMac()

    def crear_ventana(self):
        return VentanaMac()


class Aplicacion:

    def __init__(self, fabrica: FabricaUI):
        self.fabrica = fabrica

    def dibujar(self):

        boton = self.fabrica.crear_boton()
        ventana = self.fabrica.crear_ventana()

        ventana.abrir()
        boton.renderizar()


def main():

    print("=== Aplicación para Windows ===")
    app_windows = Aplicacion(FabricaWindows())
    app_windows.dibujar()

    print("\n=== Aplicación para macOS ===")
    app_mac = Aplicacion(FabricaMac())
    app_mac.dibujar()


if __name__ == "__main__":
    main()