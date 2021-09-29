import socket

IPADDR = "127.0.0.1"
PORT = 49152

sock = socket.socket(socket.AF_INET)
sock.connect((IPADDR, PORT))

# 送信無限ループ
while True:
    # 任意の文字を入力
    data = input("> ")
    # サーバーに送信
    sock.send(data.encode("utf-8"))