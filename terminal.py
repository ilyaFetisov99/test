import socket


def sendmess(i):
    ir = i.replace("send", "")
    print(ir)


def connect(ip):
    ipr = ip.replace("connect", "")
    ipr2 = ipr.replace(" ", "")
    s = socket.socket()
    s.connect((ipr2, 9090))


def command():
    i = input("User=>")
    if "send" in i:
        sendmess(i)
    elif "connect" in i:
        connect(i)
    else:
        print("Неизвестная комманда")


while True:
    command()
