#Gv1989a+wolf
import smtplib
import  requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

while True:
    resp = requests.get("https://adventofcode.com/2024/day/7")
    print(resp.status_code)
    if resp.ok:
        print("all is ok\n")
        out1=open("task.html", "w")
        out1.write(resp.text)
        out1.close()
        print("written\n")

        server_address = "smtp.mail.ru"
        server_port = 465
        login, password = "gervit2008@mail.ru", "Gv1989a+wolf"

        print("data\n")
        msg = MIMEMultipart()
        msg['From'], msg['To'], msg['Subject'] = login, "VYuGerasimov@vniief.ru", "AOC"
        msg.attach(MIMEText("Content", 'plain'))
        print("msg\n")

        file_path = "task.html"
        with open(file_path, "rb") as file:
            print("file opened\n")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={file_path}")

        print('file done into part\n')
        msg.attach(part)
        print("attached\n")
        with smtplib.SMTP(server_address, server_port) as server:
            print("start smtp\n")
            server.starttls()
            print("tls\n")
            resp_code, response = server.login(login, password)
            print(resp_code, response)
            if resp_code < 400:
                server.send_message(msg)
            else:
                print("Auth is failed!")
        break