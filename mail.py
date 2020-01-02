import smtplib
import os

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

sistem="ytbsistemi@gmail.com"
sifre="Ytbs4545."

sistemalici="yusufkorucuuu@gmail.com"
duzen=sistemalici.split(",")
gorevlialici="osolmaz@outlook.com"

s.login(sistem, sifre)

sistem_mesaji = "Yangin Durumu"
konu="Yangin Tespiti"


s.sendmail(sistem, sistemalici, konu,)

s.quit()
