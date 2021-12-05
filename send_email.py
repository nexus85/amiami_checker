import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

def send_mail(link, email, password, to_email):
    EMAIL = email
    EMAIL_PASSWORD = password
    TO_EMAIL = to_email

    smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
    smtpObj.starttls()
    smtpObj.login(EMAIL, EMAIL_PASSWORD)

    message = MIMEMultipart("alternative")
    message["Subject"] = "Кукла снова доступна для заказа"
    message["From"] = EMAIL
    message["To"] = TO_EMAIL

    text = f"""\
    Кукла снова доступна для заказа, ссылка {link}"""
    part = MIMEText(text, "plain")
    message.attach(part)

    smtpObj.sendmail(EMAIL, TO_EMAIL, message.as_string())
    smtpObj.quit()