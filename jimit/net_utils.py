#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/6/26'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'


from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

"""
Reference: [
    https://docs.python.org/2/library/email.html,
    http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html,
    http://www.tutorialspoint.com/python/python_sending_email.htm
]
"""

class NetUtils(object):

    @staticmethod
    def smtp_init(host='', port=None, login_name='', password='', tls=False):
        if port is None:
            if tls:
                tls = 587
            else:
                tls = 25

        smtp_server = SMTP(host, port)
        if tls:
            smtp_server.starttls()
        smtp_server.login(login_name, password)
        return smtp_server

    @staticmethod
    def send_mail(smtp_server=None, sender='', receivers=None, title='', message='', html=False, attachments=None):
        """
        :rtype : dict
        :param smtp_server: 一个已建立好连接的smtp实例
        :param sender: 发送者邮件地址('sender@jimit.cc')
        :param receivers: 收件者们的地址(['user1@jimit.cc', 'user2@jimit.cc'])
        :param title: 邮件标题('这是一个测试邮件')
        :param message: 邮件内容('Hello!')
        :param html: 邮件内容类型是否为html格式
        :param attachments: 附件列表，类型为MIMEImage
        :return: 返回发送结果
        """
        if receivers is None:
            receivers = []

        if attachments is None:
            attachments = []

        if smtp_server is None:
            raise ValueError('smtp_server must is not None.')

        mail = MIMEMultipart()
        mail['Subject'] = title
        mail['From'] = sender
        mail['To'] = ','.join(receivers)

        if html:
            message = MIMEText(message, "html", 'utf8')
        else:
            message = MIMEText(message, "plain", 'utf8')

        mail.attach(message)
        for attachment in attachments:
            mail.attach(attachment)

        return smtp_server.sendmail(sender, receivers, mail.as_string())
