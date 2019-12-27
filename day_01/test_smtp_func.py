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


def setup_function():
    smtp_data['smtp'].connect(host=smtp_data['smtpserver'], port=smtp_data['smtpport'])
    smtp_data['smtp'].login(smtp_data['username'], smtp_data['password'])
    print('login success')


def teardown_function():
    smtp_data['smtp'].quit()
    print('disconnecting')


def test_send_text():
    # 邮件发送、接收人员，邮件标题、正文
    msg = MIMEText('测试邮件MIMEText_01', 'plain', 'utf-8')
    msg["From"] = smtp_data['sender']
    msg["To"] = smtp_data['receivers']
    msg["Subject"] = Header("测试邮件_01", "utf-8")
    # 发送邮件
    smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())


def test_send_html():
    msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
                   "html", 'utf-8')
    msg["From"] = smtp_data['sender']
    msg["To"] = smtp_data['receivers']
    msg["Subject"] = Header("测试邮件_04", "utf-8")
    smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())


if __name__ == "__main__":
    pytest.main()
