from concurrent.futures import thread
import socket
import threading
import tkinter as tk

HEADER = 64
FORMAT="utf-8"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())#gets ip addresss automatically
print(SERVER)
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
class ServerPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        self.conn = None

        #ui


        # Message display
        self.text_box = tk.Text(self, state="disabled")
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)
        self.text_box.tag_config("sent",
        background="#1e3a6e",
        foreground="#e8eaf0",
        justify="right",
        lmargin1=80, lmargin2=80,
        rmargin=10,
        spacing1=6, spacing3=6
        )

        self.text_box.tag_config("received",
            background="#161929",
            foreground="#e8eaf0",
            justify="left",
            lmargin1=10, lmargin2=10,
            rmargin=80,
            spacing1=6, spacing3=6
        )
        # Input row
        input_frame = tk.Frame(self)
        input_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.entry = tk.Entry(input_frame)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.on_send)

        tk.Button(input_frame, text="Send",
                  command=self.on_send).pack(side="right")
        thread = threading.Thread(target=self.start_server, daemon=True)
        thread.start()
    def send(self,msg):
        print(f"sending: {msg}") 
        message = msg.encode(FORMAT)
        msg_len = len(message)
        send_length = str(msg_len).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.conn.send(send_length)
        self.conn.send(message)


    def start_server(self):
        self.server.listen(1)
        self.after(0, self.display_sent, "Waiting for connection...")
        conn, addr = self.server.accept()  # blocks until client connects
        self.after(0, self.display_sent, f"Connected: {addr}")
        while True:  # receive loop
            msg_len = conn.recv(HEADER).decode(FORMAT)
            if msg_len:
                msg_len = int(msg_len)
                msg = conn.recv(msg_len).decode(FORMAT)
                self.after(0, self.display_received, "User: \n " + msg)    

        

        

    def on_send(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            self.display_sent("You: \n" + msg)
            self.send(msg)
            self.entry.delete(0, "end")

    def display_sent(self, msg):
        self.text_box.config(state="normal")
        self.text_box.insert("end", f"  {msg}  \n", "sent")
        self.text_box.config(state="disabled")
        self.text_box.see("end")

    def display_received(self, msg):
        self.text_box.config(state="normal")
        self.text_box.insert("end", f"  {msg}  \n", "received")
        self.text_box.config(state="disabled")
        self.text_box.see("end")

