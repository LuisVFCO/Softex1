from observer import NotificacaoEmail, NotificadorSMS
from sujeito import sessao 

observer1_email = NotificacaoEmail("emailUM@hotmail.com", "Quando a Luz Morre")
observer1_sms = NotificadorSMS("+55 81 95678-9012", "Quando a Luz Morre")

observer2_email = NotificacaoEmail("emailDOIS@gmail.com", "Quando a Luz Morre")
observer2_sms = NotificadorSMS("+55 81 91234-5678", "Quando a Luz Morre")

observer3_email = NotificacaoEmail("emailTRES@outlook.com", "Quando a Luz Morre")
observer3_sms = NotificadorSMS("+55 81 98765-1234", "Quando a Luz Morre")


ses = sessao()

ses.mensagem(email=observer1_email)
ses.mensagem(sms=observer1_sms)

ses.mensagem(email=observer2_email)
ses.mensagem(sms=observer2_sms)

ses.mensagem(email=observer3_email)
ses.mensagem(sms=observer3_sms)


msg = "Informamos que a sessão foi cancelada, contate-nos para saber mais!"

ses.cancelar(msg)