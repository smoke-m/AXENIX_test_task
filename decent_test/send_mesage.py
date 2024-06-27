import datetime
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sender(email_recipient='admin@yandex.ru'):
    server_address = "smtp.yourprovider.com"
    server_port = 587  # для mail.ru 25
    login, password = "почта отправителя", "пароль"
    msg_text = f"Таблица обновленна {datetime.datetime.now()}"

    msg = MIMEMultipart()
    msg['From'], msg['To'], msg['Subject'] = (
        "почта отправителя", email_recipient, "Таблица")
    msg.attach(MIMEText(msg_text, 'plain'))

    file_path = "files/data.xls"
    file_name = "Data"
    with open(file_path, "rb") as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition', f"attachment; filename={file_name}"
        )

    msg.attach(part)
    with smtplib.SMTP(server_address, server_port) as server:
        server.starttls()
        server.login(login, password)
        server.send_message(msg)
