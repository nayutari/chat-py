import socket
# スレッドライブラリ取り込み
import threading

IPADDR = "127.0.0.1"
PORT = 49152

sock_sv = socket.socket(socket.AF_INET)
sock_sv.bind((IPADDR, PORT))
sock_sv.listen()

# データ受信ループ関数
def recv_client(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf-8"))

# クライアント接続ループ
while True:
    # クライアントの接続受付
    sock_cl, addr = sock_sv.accept()
    # スレッドクラスのインスタンス化
    thread = threading.Thread(target=recv_client, args=(sock_cl, addr))
    # スレッド処理開始
    thread.start()
