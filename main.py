import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from bs4 import BeautifulSoup
import lxml
import smtplib
from requests_html import HTMLSession
EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')

URL = "https://www.amiami.com/eng/detail?scode=FIGURE-134393&rank="
s = HTMLSession()
response = s.get(URL)
response.html.render(wait=5, retries=3, scrolldown=2, sleep=5)
about = response.html.find('.item-detail__operation__inner', first=True)

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



try:
    STATUS = False
    soup = BeautifulSoup(about.raw_html, 'lxml')
    spans = soup.find_all('span', class_='btn-cart')
    for s in spans:
        if (s.get_attribute_list('style')) == ["display: none;"] and s.text == 'Pre-orders Closed':
            STATUS = True
    if STATUS == True:
        send_mail(URL, EMAIL, EMAIL_PASSWORD, TO_EMAIL)
    else:
        pass
except:
    pass



