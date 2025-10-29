class NotificacaoEmail:
    def __init__(self, email, filme):
        self.__email = email
        self.__filme = filme

    def notifica(self, msg):
        print(f"Olá usuário de Email {self.__email} - Sessão do Filme: {self.__filme} - {msg}")

class NotificadorSMS:
    def __init__(self, sms, filme):
        self.__sms = sms
        self.__filme = filme
    
    def notificasms(self, msg):
        if len(msg) > 20:
            mensagem_curta = msg[:20] + "..."
        else:
            mensagem_curta = msg
        print(f"Olá usuário de número {self.__sms} - Sessão do Filme: {self.__filme} - {mensagem_curta}")

