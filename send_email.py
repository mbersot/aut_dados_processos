import yagmail

from playwright.sync_api import sync_playwright

def enviar_email(usuario, senha, destinatario, assunto, corpo, anexo):
    #yagmail.register(usuario, senha)
    with yagmail.SMTP(usuario, senha) as yag:
        print("Enviando e-mail!")
        yag.send(
            to=destinatario,
            subject=assunto,
            contents=corpo,
            attachments=anexo,
        )
        print("E-mail enviado com sucesso!")
