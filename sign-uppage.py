import customtkinter as ctk

def enter():
    print("enter")

# Global appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#main window
root = ctk.CTk()
root.title("Signup_Page")
root.geometry("1152x720")

# Main background frame
main_frame = ctk.CTkFrame(root, fg_color="#171923")
main_frame.pack(fill="both", expand=True)

# Outer Logo (placed on the main frame)
logo = ctk.CTkLabel(main_frame, text="🌍KULTURE", font=("Black Italic", 96, "bold", "italic"), text_color="#DC2F02")

logo.place(relx=0.5, rely=0.12, anchor="center")

# Center Login Card frame
login_frame = ctk.CTkFrame(main_frame, width=491, height=568, corner_radius=20, fg_color="#282C3E")

login_frame.place(relx=0.5, rely=0.6, anchor="center")


login_frame.pack_propagate(False)

# Inside Login Frame: Title
login_text = ctk.CTkLabel(login_frame, text="Login", font=("Black Italic", 40, "bold", "italic"))

login_text.pack(pady=(25, 30))

#  Inside Login Frame: Username Section
username_label = ctk.CTkLabel(login_frame, text="Username", font=("Black Italic", 40, "bold", "italic"), text_color="#FFFFFF")

username_label.pack(anchor="w", padx=40)

username_entry = ctk.CTkEntry(login_frame, width=415, height=59, corner_radius=20,fg_color="#383E5A")

username_entry.pack(pady=10)

#  Inside Login Frame: Password Section
password_label = ctk.CTkLabel(login_frame, text="Password", font=("Black Italic", 40, "bold", "italic"), text_color="#FFFFFF")

password_label.pack(anchor="w", padx=40, pady=(10, 0))

password_entry = ctk.CTkEntry(login_frame, width=415, height=59, corner_radius=20, show="*", fg_color="#383E5A")

password_entry.pack(pady=10)

#Enter button
enter_button = ctk.CTkButton(login_frame, text="Enter", width=240, height=79, corner_radius=35, fg_color="#171923",
                           font=("Black Italic", 24, "bold", "italic"), text_color="#FFFFFF", command=enter)
enter_button.pack(pady=(1, 25))


root.mainloop()