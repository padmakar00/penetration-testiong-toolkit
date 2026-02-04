import socket

def execute(target, port=80):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((target, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024)
        s.close()
        return {"banner": banner.decode(errors="ignore")}
    except Exception as e:
        return {"error": str(e)}
