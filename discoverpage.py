import tkinter as tk
from pathlib import Path  # Modern and secure filesystem path management
from PIL import ImageTk, Image

from connect_panel import ConnectPanel
from server import *
from server import ServerPage

class ImageTextWidget(tk.Frame):
    def __init__(self, parent, main_image_name, username_text, caption_text, pfp_name, *args, **kwargs):
        bg_color = kwargs.get("bg", "#171923")
        super().__init__(parent, *args, **kwargs)
        self.config(bg=bg_color)
        
        # Absolute path resolution ensures images load regardless of where the launcher file runs
        current_dir = Path(__file__).parent.resolve()
        pfp_path = current_dir / pfp_name
        main_image_path = current_dir / main_image_name
        
        # Open and resize the profile picture (32x32 pixels)
        pfp_image = Image.open(pfp_path)
        resized_pfp = pfp_image.resize((32, 32), Image.Resampling.LANCZOS)
        self.pfp_obj = ImageTk.PhotoImage(resized_pfp)
        
        # Open and resize the main post image (300x200 pixels)
        main_image = Image.open(main_image_path)
        resized_main = main_image.resize((300, 200), Image.Resampling.LANCZOS)
        self.main_img_obj = ImageTk.PhotoImage(resized_main)

        self.header_frame = tk.Frame(self, bg=bg_color)
        self.header_frame.pack(side="top", fill="x", anchor="w", pady=(0, 8))

        self.pfp_label = tk.Label(self.header_frame, image=self.pfp_obj, bg=bg_color)
        self.pfp_label.image = self.pfp_obj  # Memory protection reference
        self.pfp_label.pack(side="left", padx=(0, 8))

        self.username_label = tk.Label(self.header_frame, text=username_text, fg="white", bg=bg_color, font=("Arial", 12, "bold"))
        self.username_label.pack(side="left")

        self.image_label = tk.Label(self, image=self.main_img_obj, bg=bg_color)
        self.image_label.image = self.main_img_obj  # Memory protection reference
        self.image_label.pack(side="top", anchor="w", pady=(0, 6))

        # wraplength=300 ensures text wraps perfectly inside the new image boundaries
        self.caption_label = tk.Label(self, text=caption_text, fg="#E2E8F0", bg=bg_color, 
                                    font=("Arial", 10), justify="left", wraplength=300)
        self.caption_label.pack(side="top", anchor="w")


class DiscoverPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        bg_color = kwargs.get("bg", "#171923")
        super().__init__(parent, *args, **kwargs)
        self.config(bg=bg_color)
        
        self.posts = [] 

        self.canvas = tk.Canvas(self, bg=bg_color, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y") 

        self.scrollable_inner_frame = tk.Frame(self.canvas, bg=bg_color)
        self.canvas_frame_window = self.canvas.create_window((0, 0), window=self.scrollable_inner_frame, anchor="nw")

        self.scrollable_inner_frame.grid_columnconfigure(0, weight=1, pad=20)
        self.scrollable_inner_frame.grid_columnconfigure(1, weight=1, pad=20)

        self.scrollable_inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind("<Enter>", self.on_mouse_enter)
        self.canvas.bind("<Leave>", self.on_mouse_leave)


        post_data = [
            {"img": "othedev.png", "pfp": "joshua1.png", "user": "agbadev_josh", "caption": "Cooking in the morning is a scam"},
            {"img": "divine2.png", "pfp": "divine1.png", "user": "divinest_of_them_all", "caption": "Went to the museum"},
            {"img": "peace1.png", "pfp": "peace2.png", "user": "peacebeuntoyou", "caption": "Must it rain everyday i dont get"},
            {"img": "ebube2.png", "pfp": "ebube1.png", "user": "Neonwise_7", "caption": "new codes, dm for more info"},
            {"img": "mahfuz2.png", "pfp": "mahfuz1.png", "user": "fuzfuz08!", "caption": "This museum e get as e be"},
            {"img": "brian1.png", "pfp": "brian2.png", "user": "Oga_Brine", "caption": "tufffffffffffffff"}
        ]

        



        for i in range(6):
            row_idx = i // 2
            col_idx = i % 2
            current_post = post_data[i]
            
            widget_instance = ImageTextWidget(
                parent=self.scrollable_inner_frame,
                main_image_name=current_post["img"],
                pfp_name=current_post["pfp"],
                username_text=current_post["user"],
                caption_text=current_post["caption"],
                bg="#171923"
            )
            widget_instance.grid(row=row_idx, column=col_idx, padx=25, pady=25, sticky="nw")
            self.posts.append(widget_instance)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame_window, width=event.width)

    def on_mouse_enter(self, event):
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def on_mouse_leave(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


class DiscoverPage(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Discover Page")
        self.geometry("1148x656")
        self.config(bg="#171923")
        self.resizable(False, False)

        self.dashframe = tk.Frame(self, bg="#282C3E", width=178, height=656, bd=3)
        self.dashframe.pack_propagate(False)
        self.dashframe.pack(side="left", fill="y")

        # Dynamic internal path checking to stop image collection bugs
        current_dir = Path(__file__).parent.resolve()
        discover_path = current_dir / "discovericon.png"
        message_path = current_dir / "connecticon.png"
        connect_path = current_dir / "messageicon.png"

        self.discovericon = ImageTk.PhotoImage(Image.open(discover_path))
        self.messageicon = ImageTk.PhotoImage(Image.open(message_path))
        self.connecticon = ImageTk.PhotoImage(Image.open(connect_path))

        self.main_view_container = tk.Frame(self, bg="#171923")
        self.main_view_container.pack(side="left", fill="both", expand=True, padx=40, pady=40)

        self.panels = {}

        for PanelClass in (DiscoverPanel, ConnectPanel, ServerPage):
            panel_name = PanelClass.__name__
            instance = PanelClass(parent=self.main_view_container)
            self.panels[panel_name] = instance
            instance.grid(row=0, column=0, sticky="nsew")

        self.main_view_container.grid_rowconfigure(0, weight=1)
        self.main_view_container.grid_columnconfigure(0, weight=1)

        self.dbutton = tk.Button(self.dashframe, image=self.discovericon, bg="#282C3E", bd=0, command=self.show_discover)
        self.dbutton.pack(side="top", pady=(45, 37))
        self.dbutton.image = self.discovericon  # Retain visibility reference

        self.mbutton = tk.Button(self.dashframe, image=self.messageicon, bg="#282C3E", bd=0, command=self.show_messages)
        self.mbutton.pack(side="top", pady=(0, 45))
        self.mbutton.image = self.messageicon  # Retain visibility reference

        self.cbutton = tk.Button(self.dashframe, image=self.connecticon, bg="#282C3E", bd=0, command=self.show_connect)
        self.cbutton.pack(side="top", pady=(0, 37))
        self.cbutton.image = self.connecticon  # Retain visibility reference

        self.panels["DiscoverPanel"].tkraise()

    def show_discover(self):
        self.panels["DiscoverPanel"].tkraise()

    def show_messages(self):
        self.panels["ConnectPanel"].tkraise()

    def show_connect(self):
        self.panels["ServerPage"].tkraise()