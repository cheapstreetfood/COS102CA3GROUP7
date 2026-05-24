import socket
import threading
import tkinter as tk

HEADER = 64
FORMAT = "utf-8"
PORT = 5050
SERVER = "172.28.64.161"
ADDR = (SERVER, PORT)

def send(msg):
    message = msg.encode(FORMAT)
    send_length = str(len(message)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

class BubbleChat(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, bg="#0d0f1a", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        #holds the bubbles
        self.bubble_frame = tk.Frame(self.canvas, bg="#0d0f1a")
        self.canvas_window = self.canvas.create_window((0, 0), window=self.bubble_frame, anchor="nw")
        self.bubble_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(1)  # auto scroll to bottom

    def _on_canvas_configure(self, event):

        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def add_bubble(self, msg, side="left"):
        is_right = side == "right"
        bubble_color = "#1e3a6e" if is_right else "#2a2d3e"
        text_color = "#e8eaf0"

        row = tk.Frame(self.bubble_frame, bg="#0d0f1a")
        row.pack(fill="x", padx=10, pady=4)

        bubble = tk.Label(
            row,
            text=msg,
            bg=bubble_color,
            fg=text_color,
            wraplength=220,        # wrap long messages
            justify="left",
            padx=12, pady=8,
            font=("Arial", 11),
            relief="flat",
            bd=0
        )

        if is_right:
            bubble.pack(side="right")
        else:
            bubble.pack(side="left")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SocketChat")
        self.geometry("400x500")
        self.configure(bg="#0d0f1a")

        self.chat = BubbleChat(self)
        self.chat.pack(fill="both", expand=True)

        input_frame = tk.Frame(self, bg="#0d0f1a")
        input_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.entry = tk.Entry(input_frame, bg="#1e2030", fg="#e8eaf0",
                              insertbackground="white", relief="flat", font=("Arial", 11))
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0,8))
        self.entry.bind("<Return>", self.on_send)
        

        tk.Button(input_frame, text="Send", command=self.on_send,
                  bg="#1e3a6e", fg="white", relief="flat",
                  padx=12, pady=6).pack(side="right")

    def on_send(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            self.chat.add_bubble(msg, side="right")
            send(msg)
            self.entry.delete(0, "end")

    def display_received(self, msg):
        self.chat.add_bubble(msg, side="left")


def receive(app):
    app.after(0, app.display_received, f"connected to {SERVER}")
    while True:
        msg_len = client.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg = client.recv(int(msg_len)).decode(FORMAT)
            app.after(0, app.display_received, msg)

app = App()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
threading.Thread(target=receive, args=(app,), daemon=True).start()
app.mainloop()