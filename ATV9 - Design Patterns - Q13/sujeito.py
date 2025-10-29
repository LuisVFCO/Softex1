class sessao:
    def __init__(self):
        self.__emails = []
        self.__sms = []
    
    def cancelar(self, msg) -> None:
        if msg == "":
            return
        else:
            for email in self.__emails:
                email.notifica(msg)
            for sms in self.__sms:
                sms.notificasms(msg)

    def mensagem(self, email=None, sms=None):
        if email:
            self.__emails.append(email)
        elif sms:
            self.__sms.append(sms)