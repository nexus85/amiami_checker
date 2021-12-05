import datetime
import os
import time
from bs4 import BeautifulSoup
import lxml
import smtplib
from send_email import send_mail
from requests_html import HTMLSession
from csv_file import write_check, read_check, count_check


EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')

# URL = "https://www.amiami.com/eng/detail/?gcode=FIGURE-133759"
# URL = "https://www.amiami.com/eng/detail?scode=FIGURE-134393&rank="

with open('link', 'r') as f:
    URL = f.read()


s = HTMLSession()
response = s.get(URL)
response.html.render(wait=5, retries=3, scrolldown=2, sleep=5)
about = response.html.find('.item-detail__operation__inner', first=True)

date_time_now = datetime.datetime.now()
date_time_day = date_time_now.strftime("%Y.%m.%d")
date_time_time = date_time_now.strftime("%H.%M.%S")



try:
    STATUS = read_check()
    count_check(5)
    soup = BeautifulSoup(about.raw_html, 'lxml')
    spans = soup.find_all('span', class_='btn-cart')
    for s in spans:
        if (s.get_attribute_list('style')) == ["display: none;"] and s.text == 'Pre-orders Closed':
            if STATUS != True:
                send_mail(URL, EMAIL, EMAIL_PASSWORD, TO_EMAIL)
                STATUS = True
                write_check(f'{date_time_day};{date_time_time};{STATUS}\n')
            else:
                write_check(f'{date_time_day};{date_time_time};{STATUS}\n')

        elif (s.get_attribute_list('style')) == [""] and s.text == 'Pre-orders Closed':
            if STATUS != False:
                STATUS = False
                write_check(f'{date_time_day};{date_time_time};{STATUS}\n')
            else:
                write_check(f'{date_time_day};{date_time_time};{STATUS}\n')
except:
    write_check(f'{date_time_day};{date_time_time};Error\n')




