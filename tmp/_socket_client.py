# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("www.baidu.com", 80))

# s.send(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n")

# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break

# data = b''.join(buffer)

# s.close()

# header, html = data.split(b"\r\n\r\n", 1)
# print(header.decode("utf-8"))

# with open("baidu.html", "wb") as f:
#     f.write(html)


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8999))
print(s.recv(1024).decode("utf-8"))
for data in [b"Michael", b"Tracy", b"Sarah"]:
    s.send(data)
    print(s.recv(1024).decode("utf-8"))
s.send(b"exit")
s.close()
