import socket
import threading


ya_socet = socket.socket()
addr = ("127.0.0.1", 55555)
ya_socet.connect(addr)
my_name = b"Roman"
ya_socet.send(my_name)

def send_mess():
    while True:
        mes = input()
        ya_socet.send(mes.encode(encoding='ascii'))

def get_mess():
    while True:
        text = ya_socet.recv(1024)
        print(text)


rec_thread = threading.Thread(target=send_mess)
get_thread = threading.Thread(target=get_mess)
rec_thread.start()
get_thread.start()