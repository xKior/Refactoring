from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        pass

class EmailNotification(NotificationSender):
    def send(self, message: str, recipient: str) -> None:
        print(f"[EMAIL] Enviando a {recipient}: {message}")

class SMSNotification(NotificationSender):
    def send(self, message: str, recipient: str) -> None:
        print(f"[SMS] Enviando a {recipient}: {message}")

class PushNotification(NotificationSender):
    def send(self, message: str, recipient: str) -> None:
        print(f"[PUSH] Enviando a {recipient}: {message}")

class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message: str, recipient: str) -> None:
        self.sender.send(message, recipient)

def main():
    email_service = NotificationService(EmailNotification())
    sms_service = NotificationService(SMSNotification())
    push_service = NotificationService(PushNotification())

    email_service.notify("Tu pedido fue enviado", "cliente@email.com")
    sms_service.notify("Tu código de verificación es 1234", "+573001112233")
    push_service.notify("Tienes una nueva actualización", "user123")

if __name__ == "__main__":
    main()
