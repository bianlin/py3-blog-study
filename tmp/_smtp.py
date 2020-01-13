#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))


# from_addr = input("From:")
# password = input("Password:")
# to_addr = input("To:")
# smtp_server = input("Smtp Server:")

from_addr = "bianlin1987@sina.com"
password = "2d8ad0fd868ae1fa"
to_addr = "1440702000@qq.com"
smtp_server = "smtp.sina.com"


# msg = MIMEText("hello, send by Python...\n", "plain", "utf-8")
msg = MIMEText(
    "<html><body><h1>Hello</h1>"
    + '<p>send by <a href="http://www.baidu.org">Baidu</a>...</p>'
    + "</body></html>",
    "html",
    "utf-8",
)
msg["From"] = _format_addr("Python爱好者 <%s>" % from_addr)
msg["To"] = _format_addr("管理员 <%s>" % to_addr)
msg["Subject"] = Header("来自SMTP的问候......", "utf-8").encode()


server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
