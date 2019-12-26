import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

import pytest


class TestSmtp():
    sender = '515199703@qq.com'
    receivers = '515199703@qq.com'
    smtpserver = 'smtp.qq.com'
    smtpport = 465

    username = '515199703@qq.com'
    password = 'ivfrbelfzqvbbhfi'
    smtp = smtplib.SMTP_SSL(smtpserver)

    @classmethod
    def setup_class(cls):
        cls.smtp.connect(host=cls.smtpserver, port=cls.smtpport)
        cls.smtp.login(cls.username, cls.password)
        print('login success')

    @classmethod
    def teardown_class(cls):
        cls.smtp.quit()
        print('disconnecting')

    def test_send_text(self):
        # 邮件发送、接收人员，邮件标题、正文
        msg = MIMEText('测试邮件MIMEText_01', 'plain', 'utf-8')
        msg["From"] = self.sender
        msg["To"] = self.receivers
        msg["Subject"] = Header("测试邮件_01", "utf-8")
        # 发送邮件
        self.smtp.sendmail(self.sender, self.receivers, msg.as_string())

    def test_send_html(self):
        msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
                       "html", 'utf-8')
        msg["From"] = self.sender
        msg["To"] = self.receivers
        msg["Subject"] = Header("测试邮件_02", "utf-8")
        self.smtp.sendmail(self.sender, self.receivers, msg.as_string())

    def test_send_attachment(self):
        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = self.receivers
        msg["Subject"] = Header("测试邮件_03", "utf-8")
        # 构建带附件的邮件正文
        msg.attach(MIMEText('测试邮件MIMEText_03', 'plain', 'utf-8'))
        # 构造附件,多个附件同理
        attach1 = MIMEText(open("smtp.json",'rb').read(), "base64", "utf-8")
        attach1["Content-Type"] = "application/octet-stream"

        # 这里filename随意写，将会在邮件中显示
        attach1["Content-Disposition"] = "attrachment;filename=data.txt"

        # 关联附件到正文
        msg.attach(attach1)
        # 发送邮件
        self.smtp.sendmail(self.sender, self.receivers, msg.as_string())


if __name__ == "__main__":
    pytest.main()
