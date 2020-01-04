import smtplib
import os

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

sistem="example@gmail.com"
sifre="pass."

sistemalici="yusufkorucuuu@gmail.com"

s.login(sistem, sifre)

sistem_mesaji = "Yangin Durumu"
konu="Yangin Tespiti"


s.sendmail(sistem, sistemalici, konu,)

s.quit()
