import socket
import threading
import tkinter

# -- tkinter による GUI の初期化
root = tkinter.Tk()
root.title("nayutari chat")
root.geometry("400x300")

scrl_frame = tkinter.Frame(root)
scrl_frame.pack()

listbox = tkinter.Listbox(scrl_frame, width=40, height=15)
listbox.pack(side=tkinter.LEFT)

scroll_bar = tkinter.Scrollbar(scrl_frame, command=listbox.yview)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox.config(yscrollcommand=scroll_bar.set)

input_frame = tkinter.Frame(root)
input_frame.pack()

textbox = tkinter.Entry(input_frame)
textbox.pack(side=tkinter.LEFT)

button = tkinter.Button(input_frame, text="send")
button.pack(side=tkinter.RIGHT)

# データ受信時のコールバック関数
def on_recv_data(data):
    listbox.insert(tkinter.END, data)
    listbox.yview_moveto(1)

# -- 通信まわりの初期化
IPADDR = "127.0.0.1"
PORT = 49152

sock = socket.socket(socket.AF_INET)
sock.connect((IPADDR, PORT))

def recv_loop(sock, on_recv_func):
    while True:
        try:
            data = sock.recv(1024)
            if data == b"":
                break
            # 受信コールバック呼び出し
            on_recv_func(data.decode("utf-8"))
        except ConnectionResetError:
            break

    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

thread = threading.Thread(target=recv_loop, args=(sock, on_recv_data))
thread.start()

# 送信ボタンクリック時のコールバック
def on_send_click(sock):
    data = textbox.get()
    sock.send(data.encode("utf-8"))
    textbox.delete(0, tkinter.END)

button.configure(command=lambda:on_send_click(sock))

root.mainloop()

sock.shutdown(socket.SHUT_RDWR)
sock.close()