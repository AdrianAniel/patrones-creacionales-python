from abc import ABC, abstractmethod


class Notificacion(ABC):

    @abstractmethod
    def enviar(self, mensaje):
        pass


class NotificacionEmail(Notificacion):

    def enviar(self, mensaje):
        print(f"[EMAIL] Enviando correo: {mensaje}")


class NotificacionSMS(Notificacion):

    def enviar(self, mensaje):
        print(f"[SMS] Enviando mensaje de texto: {mensaje}")


class NotificacionPush(Notificacion):

    def enviar(self, mensaje):
        print(f"[PUSH] Enviando notificación al móvil: {mensaje}")


class CreadorNotificacion(ABC):

    @abstractmethod
    def crear_notificacion(self):
        pass


class CreadorEmail(CreadorNotificacion):

    def crear_notificacion(self):
        return NotificacionEmail()


class CreadorSMS(CreadorNotificacion):

    def crear_notificacion(self):
        return NotificacionSMS()


class CreadorPush(CreadorNotificacion):

    def crear_notificacion(self):
        return NotificacionPush()


class Cliente:

    def __init__(self, creador):
        self.creador = creador

    def enviar_mensaje(self, mensaje):
        notificacion = self.creador.crear_notificacion()
        notificacion.enviar(mensaje)


def main():

    mensaje = "¡Ofertino detectó una rebaja del 80% en Terraria!"

    print("=== Notificación por Email ===")
    cliente_email = Cliente(CreadorEmail())
    cliente_email.enviar_mensaje(mensaje)

    print("\n=== Notificación por SMS ===")
    cliente_sms = Cliente(CreadorSMS())
    cliente_sms.enviar_mensaje(mensaje)

    print("\n=== Notificación Push ===")
    cliente_push = Cliente(CreadorPush())
    cliente_push.enviar_mensaje(mensaje)


if __name__ == "__main__":
    main()