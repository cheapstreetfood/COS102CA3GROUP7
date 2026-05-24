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
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        self.conn = None


        
        # CHAT AREA CONTAINER
        # CHAT AREA
        chat_frame = tk.Frame(self)
        chat_frame.pack(fill="both", expand=True)

        # Canvas
        self.canvas = tk.Canvas(
            chat_frame,
            bg="#0d0f1a",
            highlightthickness=0
        )

        # Scrollbar
        scrollbar = tk.Scrollbar(
            chat_frame,
            command=self.canvas.yview
        )

        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Pack INSIDE chat_frame
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Holds the bubbles
        self.bubble_frame = tk.Frame(
            self.canvas,
            bg="#0d0f1a"
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.bubble_frame,
            anchor="nw"
        )

        self.bubble_frame.bind(
            "<Configure>",
            self._on_frame_configure
        )

        self.canvas.bind(
            "<Configure>",
            self._on_canvas_configure
        )
        self.bubble_frame = tk.Frame(self.canvas, bg="#0d0f1a")
        self.canvas_window = self.canvas.create_window((0, 0), window=self.bubble_frame, anchor="nw")
        self.bubble_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        #input
        input_frame = tk.Frame(self, bg="#0d0f1a")
        input_frame.pack(fill="x", )

        self.entry = tk.Entry(input_frame, bg="#1e2030", fg="#e8eaf0",
                              insertbackground="white", relief="flat", font=("Arial", 11))
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0,8))
        self.entry.bind("<Return>", self.on_send)

        tk.Button(input_frame, text="Send", command=self.on_send,
                  bg="#1e3a6e", fg="white", relief="flat",
                  padx=12, pady=6).pack(side="right")
        thread = threading.Thread(target=self.start_server, daemon=True)
        thread.start()

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(1)  # auto scroll to bottom

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def add_bubble(self, msg, side="left"):
        is_right = side == "right"
        bubble_color = "#1e3a6e" if is_right else "#2a2d3e"
        text_color = "#e8eaf0"

        row = tk.Frame(self.bubble_frame, bg="#2b2f43")
        row.pack(fill="x", padx=10, pady=4)

        bubble = tk.Label(
            row,
            text=msg,
            bg=bubble_color,
            fg=text_color,
            wraplength=220,        # wrap messages
            justify="left",
            padx=12, pady=8,
            font=("Arial", 11),
            relief="flat",
            bd=0,
            

        )

        if is_right:
            bubble.pack(side="right")
        else:
            bubble.pack(side="left")    
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
        self.after(0, self.add_bubble, "Waiting for connection...")
        self.conn, addr = self.server.accept()  # blocks until client connects
        self.after(0, self.add_bubble, f"Connected: {addr}")
        while True:  # receive loop
            msg_len = self.conn.recv(HEADER).decode(FORMAT)
            if msg_len:
                msg_len = int(msg_len)
                msg = self.conn.recv(msg_len).decode(FORMAT)
                self.after(0, self.add_bubble,msg)    

        

        

    def on_send(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            self.add_bubble(msg, side="right")
            self.send(msg)
            self.entry.delete(0, "end")

    
