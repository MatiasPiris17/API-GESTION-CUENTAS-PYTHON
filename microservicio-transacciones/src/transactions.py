class Remitente:
    def __init__(self, dni: str, email: str):
        self.dni = dni
        self.email = email

class Destinatario:
    def __init__(self, dni: str, email: str):
        self.dni = dni
        self.email = email

class Transactions:
    def __init__(self, remitente: Remitente, destinatario: Destinatario, transferencia: int):
        self.remitente = remitente
        self.destinatario = destinatario
        self.transferencia = transferencia