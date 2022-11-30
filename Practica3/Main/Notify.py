import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from getSNMP import consultaSNMP

COMMASPACE = ', '
# Define params
rrdpath = '/home/eduardo/Documentos/Redes 3/Practica3/RRD/'
imgpath = '/home/eduardo/Documentos/Redes 3/Practica3/IMG/'
fname = 'trend.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "lalo.olay@hotmail.com"

mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'


def send_alert_attached(subject,elementos):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    for recurso in elementos:
        fp = open(imgpath+'deteccion{}.png'.format(recurso), 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()