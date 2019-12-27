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


class TestSmtp:
    def test_send_text_01(self, smtp_ini):
        # 邮件发送、接收人员，邮件标题、正文
        msg = MIMEText('测试邮件MIMEText_01', 'plain', 'utf-8')
        msg["From"] = smtp_data['sender']
        msg["To"] = smtp_data['receivers']
        msg["Subject"] = Header("测试邮件_02", "utf-8")
        # 发送邮件
        # smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())

    @pytest.mark.skipif(smtp_data['smtpserver'] == 'smtp.163.com', reason='如果是QQ邮箱则不发送')
    def test_send_text_02(self, smtp_ini):
        # 邮件发送、接收人员，邮件标题、正文
        msg = MIMEText('测试邮件MIMEText_01', 'plain', 'utf-8')
        msg["From"] = smtp_data['sender']
        msg["To"] = smtp_data['receivers']
        msg["Subject"] = Header("测试邮件_01", "utf-8")
        # 发送邮件
        # smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())

    @pytest.mark.skip(reason='不发送该邮件')
    def test_send_text_03(self, smtp_ini):
        # 邮件发送、接收人员，邮件标题、正文
        msg = MIMEText('测试邮件MIMEText_03', 'plain', 'utf-8')
        msg["From"] = smtp_data['sender']
        msg["To"] = smtp_data['receivers']
        msg["Subject"] = Header("测试邮件_03", "utf-8")
        # 发送邮件
        # smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())

    @pytest.mark.xfail("hasattr(os, 'sep')")
    def test_send_text_04(self, smtp_ini):
        # 邮件发送、接收人员，邮件标题、正文
        msg = MIMEText('测试邮件MIMEText_04', 'plain', 'utf-8')
        msg["From"] = smtp_data['sender']
        msg["To"] = smtp_data['receivers']
        msg["Subject"] = Header("测试邮件_04", "utf-8")
        # 发送邮件
        # smtp_data['smtp'].sendmail(smtp_data['sender'], smtp_data['receivers'], msg.as_string())
        assert msg["To"] == 1


if __name__ == "__main__":
    pytest.main()
