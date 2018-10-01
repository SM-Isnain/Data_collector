from email.mime.text import MIMEText
import smtplib

def send_email(email, height, avg_height, count):
    from_email="shuprova08@gmail.com"
    from_password="Shuprova@1234"
    to_email=email
    subject="Height data from the height statistics website"
    message="Hey there, your height is <strong>%s</strong>cm. Average height of all the <strong>%s</strong> respondents is <strong>%s</strong>." % (height, count, avg_height)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
