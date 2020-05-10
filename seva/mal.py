import smtplib
def send_mail(body):

    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('manisha.khandelwal.15cse@bml.edu.in', '8952035986')
    smtpObj.sendmail('manisha.khandelwal.15cse@bml.edu.in', 'teena.khandelwal.15cse@bml.edu.in', body)  # Or recipient@outlook
    smtpObj.quit()
    pass