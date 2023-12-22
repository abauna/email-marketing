import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from google.oauth2 import service_account
import google.auth
from google.auth.transport.requests import Request

def enviar(email, assunto, destinos, mensagem_corpo, anexo=None):
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    SERVICE_ACCOUNT_FILE = 'caminho/para/o/seu/arquivo-de-credencial.json'  # Altere para o caminho do seu arquivo JSON de credencial

    creds = None
    creds, _ = google.auth.default()

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(requests())
        else:
            creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES
            )

    # Conexão segura com o servidor SMTP do Gmail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(email, creds)

        # Criação da mensagem
        mensagem = MIMEMultipart()
        mensagem['From'] = email
        mensagem['To'] = ', '.join(destinos)
        mensagem['Subject'] = assunto

        # Adiciona o corpo da mensagem
        mensagem.attach(MIMEText(mensagem_corpo, 'plain'))

        # Adiciona o anexo se existir
        if anexo:
            with open(anexo, 'rb') as arquivo_anexo:
                parte_anexo = MIMEBase('application', 'octet-stream')
                parte_anexo.set_payload(arquivo_anexo.read())
                encoders.encode_base64(parte_anexo)
                parte_anexo.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {anexo}'
                )
                mensagem.attach(parte_anexo)

        # Envio do e-mail
        server.sendmail(email, destinos, mensagem.as_string())

