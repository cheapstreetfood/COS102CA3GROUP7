import csv
import os
import tkinter as tk
from tkinter import messagebox

class ConnectPanel(tk.Frame):
#    def __init__(self, parent, *args, **kwargs):
#        super().__init__(parent, *args, **kwargs)
#        self.config(bg="#171923")
#        
#        label = tk.Label(self, text="💬 Messages Inbox", fg="white", bg="#171923", font=("Arial", 24, "bold"))
#        label.pack(expand=True)


    def __init__(self, parent, csv_filename="kulture.csv", **kwargs):
        super().__init__(parent, **kwargs)
        self.csv_filename = csv_filename

        # ==========================================
        # SECTION 1: Profile & Bio Layout
        # ==========================================
        profile_container = tk.Frame(self, bd=2, relief="groove", bg="#171923")
        profile_container.pack(fill="x", padx=10, pady=5)

        tk.Label(
            profile_container,
            text="John Doe",
            font=("Arial", 16, "bold"),
            bg="#171923",
            fg="white",
        ).pack(anchor="w", padx=10, pady=5)

        bio_text = "Software Developer. Loves coding, coffee, and building Python GUIs."
        tk.Label(
            profile_container,
            text=bio_text,
            wraplength=350,
            justify="left",
            bg="#171923",
            fg="white",
        ).pack(anchor="w", padx=10, pady=(0, 10))

        # ==========================================
        # SECTION 2: Friend List Layout
        # ==========================================
        friends_container = tk.Frame(self, bd=2, relief="groove", bg="#171923")
        friends_container.pack(fill="both", expand=True, padx=10, pady=5)

        tk.Label(
            friends_container,
            text="Friend List",
            font=("Arial", 12, "bold"),
            bg="#171923",
            fg="white",
        ).pack(anchor="w", padx=10, pady=5)

        # Internal grid container
        table_container = tk.Frame(friends_container, bg="#171923")
        table_container.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Column Header (Now just 'Name')
        tk.Label(
            table_container,
            text="Name",
            font=("Arial", 10, "bold"),
            width=30,
            bg="#171923",
            fg="white",
        ).grid(row=0, column=0, sticky="ew")

        # Listbox for friend names
        self.listbox = tk.Listbox(
            table_container,
            height=10,
            font=("Courier", 10),
            bg="#171923",
            fg="white",
        )
        self.listbox.grid(row=1, column=0, sticky="nsew")

        table_container.grid_rowconfigure(1, weight=1)
        table_container.grid_columnconfigure(0, weight=1)

        # Populate listbox on initialization
        self.load_friends_from_csv()

    def load_friends_from_csv(self):
        """Reads friend data from the local CSV file."""
        self.listbox.delete(0, tk.END)

        if not os.path.exists(self.csv_filename):
            messagebox.showerror(
                "Error", f"'{self.csv_filename}' file not found!"
            )
            self.listbox.insert(tk.END, "CSV file missing.")
            return

        try:
            with open(
                self.csv_filename, mode="r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.reader(file)
                next(reader)  # Skip headers

                for row in reader:
                    # Check if the row has data before trying to access index 0
                    if len(row) >= 1:
                        name = row[0]
                        self.listbox.insert(tk.END, name)

        except Exception as e:
            messagebox.showerror("Error", f"Could not read CSV: {e}")