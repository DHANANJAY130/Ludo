import socket
from _thread import *
import sys

server = socket.gethostname()#"127.0.0.1"
print(server)
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("waiting for a connection, Server started")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                reply += "!!"
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    # print("this is connection: ", conn) # prints the socket information

    start_new_thread(threaded_client, (conn,))