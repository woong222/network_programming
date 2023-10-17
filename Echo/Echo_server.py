from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (client_ip, client_port) = sock.accept()
print('connected by', client_ip, client_port)
while True:
    try:
        data = conn.recv(BUFSIZE)
    except:
        conn.close()
        break
    else:
        if not data:
            break
        print("Received message: ", data.decode())

    try:
        conn.send(data)
    except:
        conn.close()
        break
conn.close()