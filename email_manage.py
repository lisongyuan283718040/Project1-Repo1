import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailManage:

    def send_email(self, report_name):
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'
        # 发送邮件的用户名和客户端密码
        username = 'lisongyuan.1984@163.com'
        password = 'KUXQOLTABRCYRVZW' # 授权密码
        # 接受邮件邮箱
        receivers = '283718040@qq.com,lisongyuan84@gmail.com'
        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = 'PythonSentMultipleReports'
        attachment = MIMEText(open(report_name, 'rb').read(), 'html', 'utf-8') # 附件
        # 把邮件的信息组装到邮件对象里面
        message['from'] = username
        message['to'] = receivers
        message['subject'] = subject
        message.attach(attachment)
        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receivers.split(','), message.as_string())
        smtp.quit()

"""The below main function is only used when debugging this py file,
if using combined with test_ecshop.py, no need to use main function"""
# if __name__ == '__main__':
#     EmailManage().send_email(r'D:\pythonProject\Email\report.html')
