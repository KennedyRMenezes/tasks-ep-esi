import smtplib
import os
from email.mime.text import MIMEText


class Email():
    

    def envia_email(subject, sender, recipients, deadline, link):

        message = f"Olá aluno você está recebendo esta mensagem pois foi liberado o formulário a ser preenchido até a data de {deadline}.\nVocê consegue preencher o formulário de avaliação do semestre de pós-graduação clicando nesse link: {link}"


        # Criando a mensagem MIME com codificação UTF-8
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        # Retirado o To para os destinatários não saberem a lista de emails
        #msg['To'] = ', '.join(recipients)

        # Iniciando o servidor SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Fazendo login no servidor
        server.login(sender, 'oxji jsrr ryry mlyu')

        # Enviando o e-mail
        server.sendmail(sender, recipients, msg.as_string())

        print("Email has been sent!")

    


if __name__ == "__main__":

    sender = 'esi.code.proj@gmail.com'
    password = os.getenv('ESI_EMAIL_PASS')
    recipients = ["kennedy12kennedy@gmail.com", "menezes_kennedy@hotmail.com", "kennedy_menezes@usp.br"]
    subject = "Link para Formulário Semestral"
    deadline = "2024-12-12"
    link = "link..."


    Email.envia_email(subject, sender, recipients, deadline, link)






