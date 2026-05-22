import tkinter as tk

# Color Palette
BG_COLOR = "#171923"
ACCENT_COLOR = "#DC2F02"
text_color= "#ffffff"

#  Buttons functions
def click_discover():
    pass

def click_build():
    pass

def click_cultivate():
    pass

# main window
root = tk.Tk()
root.title("Navigation Page")
root.geometry("900x600")
root.configure(bg=BG_COLOR)

# Logo and app name frame
logo_frame = tk.Frame(root, bg=BG_COLOR)
logo_frame.pack(pady=(30, 200))

logo_label = tk.Label( logo_frame, text="🌍 KULTURE", font=("Arial Black", 48, "italic"), fg=ACCENT_COLOR, bg=BG_COLOR )
logo_label.pack()

# buttons columns
buttons_feature = tk.Frame(root, bg=BG_COLOR)
buttons_feature.pack(expand=True, fill="both", padx=40)

buttons_feature.columnconfigure(0, weight=1)
buttons_feature.columnconfigure(1, weight=1)
buttons_feature.columnconfigure(2, weight=1)

# Column 1
column1 = tk.Frame(buttons_feature, bg=BG_COLOR)
column1.grid(row=0, column=0, sticky="nsew")

tk.Label(column1, text="Discover New\nPeople", font=("black italic", 18, "bold italic"), fg=text_color, bg=BG_COLOR).pack(pady=(0, 5))
tk.Button(column1, text="🧭", font=("black italic", 60), fg=ACCENT_COLOR, bg=BG_COLOR,
          relief="flat", activebackground=BG_COLOR, activeforeground="#ff6b52", bd=0,
          cursor="hand2", command=click_discover).pack()

# Column 2
column2 = tk.Frame(buttons_feature, bg=BG_COLOR)
column2.grid(row=0, column=1, sticky="nsew")
tk.Label(column2, text="Build the\nconversation", font=("black italic", 18, "bold italic"), fg=text_color, bg=BG_COLOR).pack(pady=(0, 5))
tk.Button(column2, text="➤", font=("black italic", 60), fg=ACCENT_COLOR, bg=BG_COLOR,
          relief="flat", activebackground=BG_COLOR, activeforeground="#ff6b52", bd=0,
          cursor="hand2", command=click_build).pack()

# Column 3
column3 = tk.Frame(buttons_feature, bg=BG_COLOR)
column3.grid(row=0, column=2, sticky="nsew")
tk.Label(column3, text="Cultivate\nConnections", font=("black italic", 18, "bold italic"), fg=text_color, bg=BG_COLOR).pack(pady=(0, 5))
tk.Button(column3, text="👥", font=("black italic", 60), fg=ACCENT_COLOR, bg=BG_COLOR,
          relief="flat", activebackground=BG_COLOR, activeforeground="#ff6b52", bd=0,
          cursor="hand2", command=click_cultivate).pack()




root.mainloop()