import customtkinter as ctk
from tkinter import CENTER

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # ======== Status Label (Top Right) ========
        self.status_label = ctk.CTkLabel(
            self,
            text="Status: Running",
            text_color="#00FF7F",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.status_label.place(relx=0.95, rely=0.05, anchor="ne")

        # ======== Title ========
        self.title_label = ctk.CTkLabel(
            self,
            text="AGV System",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color="#FFFFFF"
        )
        self.title_label.place(relx=0.5, rely=0.35, anchor=CENTER)

        # ======== Auto Button ========
        self.auto_btn = ctk.CTkButton(
            self,
            text="Auto Mode",
            width=160,
            height=45,
            corner_radius=20,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#1E90FF",
            hover_color="#4682B4",
            command=self.open_auto
        )
        self.auto_btn.place(relx=0.38, rely=0.55, anchor=CENTER)

        # ======== Manual Button ========
        self.manual_btn = ctk.CTkButton(
            self,
            text="Manual Mode",
            width=160,
            height=45,
            corner_radius=20,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#32CD32",
            hover_color="#2E8B57",
            command=self.open_manual
        )
        self.manual_btn.place(relx=0.62, rely=0.55, anchor=CENTER)

        # ======== Footer ========
        self.footer_label = ctk.CTkLabel(
            self,
            text="Created by Heshala Angage | © All Rights Reserved",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.footer_label.place(relx=0.5, rely=0.95, anchor=CENTER)

    # ======== Navigation Functions ========
    def open_auto(self):
        """Navigate to Auto Mode Page"""
        self.master.show_auto_page()

    def open_manual(self):
        """Navigate to Manual Mode Page"""
        self.master.show_manual_page()
