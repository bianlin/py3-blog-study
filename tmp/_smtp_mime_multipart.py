#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))

# 1
# from_addr = "bianlin1987@sina.com"
# password = "2d8ad0fd868ae1fa"
# to_addr = "1440702000@qq.com"
# smtp_server = "smtp.sina.com"

from_addr = "xiaolin.tom.bl@gmail.com"
password = "bianlin-2009"
to_addr = "1440702000@qq.com"
smtp_server = "smtp.gmail.com"

#指定subtype是alternative, 组合一个HTML和Plain
msg = MIMEMultipart('alternative')
msg["From"] = _format_addr("Python爱好者 <%s>" % from_addr)
msg["To"] = _format_addr("管理员 <%s>" % to_addr)
msg["Subject"] = Header("来自SMTP的问候......", "utf-8").encode()

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0" /></p>'
    '</body></html>', "html", "utf-8"))

with open("D:\\pypro\\tmp\\mycat.png", "rb") as f:
    mime = MIMEBase("image", "png", filename="test.png")
    mime.add_header("Content-Disposition", "attachment", filename="test.png")
    mime.add_header("Content-ID", "<0>")
    mime.add_header("X-Attachment-Id", "0")
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
