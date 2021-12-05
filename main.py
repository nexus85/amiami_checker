import os
import time

from bs4 import BeautifulSoup
import lxml
import smtplib
from send_email import send_mail
from requests_html import HTMLSession
EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')

URL = "https://www.amiami.com/eng/detail/?gcode=FIGURE-133759"
s = HTMLSession()
response = s.get(URL)
response.html.render(wait=5, retries=3, scrolldown=2, sleep=5)
about = response.html.find('.item-detail__operation__inner', first=True)


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



