import socket
import threading
import tkinter as tk

HEADER = 64
FORMAT="utf-8"
PORT = 5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"



def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SocketChat")
        self.geometry("400x500")

        # Message display
        self.text_box = tk.Text(self, state="disabled")
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)

        # Input row
        input_frame = tk.Frame(self)
        input_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.entry = tk.Entry(input_frame)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.on_send)

        tk.Button(input_frame, text="Send",
                  command=self.on_send).pack(side="right")

    def on_send(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            self.display("You: " + msg)
            send(msg)
            self.entry.delete(0, "end")

    def display(self, msg):
        self.text_box.config(state="normal")
        self.text_box.insert("end", msg + "\n")
        self.text_box.config(state="disabled")
        self.text_box.see("end")  # auto scroll


#Receive 
def receive(app):
    print("receive loop started")
    while True:
        msg_len = client.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = client.recv(msg_len).decode(FORMAT)
            print(f"received: {msg}") 
            app.after(0, app.display, "Them: " + msg)

app=App()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
thread = threading.Thread(target=receive,args=(app,),daemon=True)
thread.start()

app.mainloop()