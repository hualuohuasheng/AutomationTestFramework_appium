import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_host = "smtp.qq.com"
mail_user = '1145930174'

mail_pass = 'brpsxxyupgqohfif'

sender = '1145930174@qq.com'

receivers = ['liml@sjdd.com.cn']

with open(f'F:/1/Test_TestStringMethods_2018-08-23_16-53-14.html','rb') as f:
    mail_body = f.read()

message = MIMEMultipart()
message['Subject'] = 'title'
message['From'] = sender
message['To'] = receivers[0]

message.attach(MIMEText(mail_body,'html','utf-8'))

puretext = MIMEText(mail_host)

try:
    # smtpObj = smtplib.SMTP()
    # smtpObj.connect(mail_host,25)
    smtpObj = smtplib.SMTP_SSL(mail_host,465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e)
    
