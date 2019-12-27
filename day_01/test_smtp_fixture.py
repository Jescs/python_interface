import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

import pytest

smtp_data = {'sender': '515199703@qq.com',
             'receivers': '515199703@qq.com',
             'smtpserver': 'smtp.qq.com',
             'smtpport': 465,
             'username': '515199703@qq.com',
             'password': 'ivfrbelfzqvbbhfi',
             'smtp': smtplib.SMTP_SSL('smtp.qq.com')}


@pytest.fixture(scope='module')
def smtp_ini():
    smtp_data['smtp'].connect(host=smtp_data['smtpserver'], port=smtp_data['smtpport'])
    smtp_data['smtp'].login(smtp_data['username'], smtp_data['password'])
    print('login success')
    yield smtp_ini
    smtp_data['smtp'].quit()
    print('disconnecting')


class TestSmtp():

    def test_send_text(self, smtp_ini):
        # 邮件发送、接收人员，邮件标题、正文
        msg = MIMEText('测试邮件MIMEText_01', 'plain', 'utf-8')
        msg["From"] = smtp_data['sender']
        msg["To"] = smtp_data['receivers']
        msg["Subject"] = Header("测试邮件_01", "utf-8")
        # 发送邮件
        smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())

    def test_send_html(self, smtp_ini):
        msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
                       "html", 'utf-8')
        msg["From"] = smtp_data['sender']
        msg["To"] = smtp_data['receivers']
        msg["Subject"] = Header("测试邮件_02", "utf-8")
        smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())


# class TestAttachment:
#     def test_send_attachment(self, smtp_ini):
#         msg = MIMEMultipart()
#         msg["From"] = smtp_data['sender']
#         msg["To"] = smtp_data['receivers']
#         msg["Subject"] = Header("测试邮件_03", "utf-8")
#         # 构建带附件的邮件正文
#         msg.attach(MIMEText('测试邮件MIMEText_03', 'plain', 'utf-8'))
#         # 构造附件,多个附件同理
#         file = "D:\code\pytest_code\python_interface\day_01\smtp.json"
#         attach1 = MIMEText(open(file, 'rb').read(), "base64", "utf-8")
#         attach1["Content-Type"] = "application/octet-stream"
#
#         # 这里filename随意写，将会在邮件中显示
#         attach1["Content-Disposition"] = "attrachment;filename=data.txt"
#
#         # 关联附件到正文
#         msg.attach(attach1)
#         # 发送邮件
#         smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())
#

def test_send_html(smtp_ini):
    msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
                   "html", 'utf-8')
    msg["From"] = smtp_data['sender']
    msg["To"] = smtp_data['receivers']
    msg["Subject"] = Header("测试邮件_04", "utf-8")
    smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())


if __name__ == "__main__":
    pytest.main()
