import customtkinter as ctk
from tkinter import CENTER

class AutoPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="AGV System",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#FFFFFF"
        )
        self.title_label.place(relx=0.5, rely=0.12, anchor=CENTER)

        # Mode Selected
        self.mode_label = ctk.CTkLabel(
            self,
            text="Mode: Auto",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#00BFFF"
        )
        self.mode_label.place(relx=0.5, rely=0.25, anchor=CENTER)

        # Battery Percentage
        self.battery_label = ctk.CTkLabel(
            self,
            text="Battery: 85%",
            font=ctk.CTkFont(size=18),
            text_color="#7CFC00"
        )
        self.battery_label.place(relx=0.5, rely=0.35, anchor=CENTER)

        # Waiting Time
        self.wait_label = ctk.CTkLabel(
            self,
            text="Waiting Time (minutes):",
            font=ctk.CTkFont(size=14)
        )
        self.wait_label.place(relx=0.35, rely=0.5, anchor=CENTER)

        self.wait_entry = ctk.CTkEntry(self, width=100, placeholder_text="0")
        self.wait_entry.place(relx=0.65, rely=0.5, anchor=CENTER)

        # Loop Count
        self.loop_label = ctk.CTkLabel(
            self,
            text="Loop Count:",
            font=ctk.CTkFont(size=14)
        )
        self.loop_label.place(relx=0.35, rely=0.6, anchor=CENTER)

        self.loop_entry = ctk.CTkEntry(self, width=100, placeholder_text="0")
        self.loop_entry.place(relx=0.65, rely=0.6, anchor=CENTER)

        # Buttons
        self.start_btn = ctk.CTkButton(
            self,
            text="Start",
            width=150,
            height=40,
            fg_color="#1E90FF",
            hover_color="#4682B4",
            corner_radius=20,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.start_btn.place(relx=0.38, rely=0.8, anchor=CENTER)

        self.home_btn = ctk.CTkButton(
            self,
            text="Home",
            width=150,
            height=40,
            fg_color="#808080",
            hover_color="#696969",
            corner_radius=20,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.go_home
        )
        self.home_btn.place(relx=0.62, rely=0.8, anchor=CENTER)

    def go_home(self):
        self.master.show_home_page()
