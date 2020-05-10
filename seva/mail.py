import smtplib


def send_mail(body):
     try:
         smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
     except Exception as e:
         print(e)
         smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
     smtpObj.ehlo()
     smtpObj.starttls()
     smtpObj.login('notifications@indxx.com', "Traffic@1234")
     smtpObj.sendmail('notifications@indxx.com', ['mkhandelwal@indxx.com'], body) # Or recipient@outlook
     smtpObj.quit()
     pass

