import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user=""    #用户名
mail_pass=""   #口令 
 
 
sender = 'noreply@steampowered.com'
receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("Steam Support", 'utf-8')
message['To'] =  Header("", 'utf-8')
 
subject = '来点测试来点测试来点测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
# try:
# smtpObj = smtplib.SMTP() 
# smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
# smtpObj.login(mail_user,mail_pass) 
# smtpObj.ehlo() 
# smtpObj.sendmail(sender, receivers, message.as_string())
# smtpObj.quit()
    # print("邮件发送成功")
# except smtplib.SMTPException:
#     print ("Error: 无法发送邮件")
# 登录发送者账号(发送前一定要登录)
server = smtplib.SMTP_SSL(mail_host, 465)
# server.connect(mail_host)
server.ehlo(mail_host)
server.login(mail_user, mail_pass)
# # 发送邮件
server.sendmail(sender, receivers, message.as_string())
# # 退出(发完后一定要退出, 不然一个小时左右之后会自动退出)
server.quit()