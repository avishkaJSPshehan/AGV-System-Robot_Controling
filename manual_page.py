import customtkinter as ctk
from tkinter import CENTER

class ManualPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # ===== Title =====
        self.title_label = ctk.CTkLabel(
            self,
            text="AGV System",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#FFFFFF"
        )
        self.title_label.place(relx=0.5, rely=0.12, anchor=CENTER)

        # ===== Battery =====
        self.battery_label = ctk.CTkLabel(
            self,
            text="Battery: 80%",
            font=ctk.CTkFont(size=18),
            text_color="#7CFC00"
        )
        self.battery_label.place(relx=0.5, rely=0.25, anchor=CENTER)

        # ===== Main Buttons (Charge / Trip) =====
        self.charge_btn = ctk.CTkButton(
            self,
            text="Charge",
            width=160,
            height=45,
            corner_radius=20,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#FFA500",
            hover_color="#FF8C00",
            command=self.show_charge_section
        )
        self.charge_btn.place(relx=0.38, rely=0.38, anchor=CENTER)

        self.trip_btn = ctk.CTkButton(
            self,
            text="Trip",
            width=160,
            height=45,
            corner_radius=20,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#1E90FF",
            hover_color="#4682B4",
            command=self.show_trip_section
        )
        self.trip_btn.place(relx=0.62, rely=0.38, anchor=CENTER)

        # ===== Home Button (Bottom Left) =====
        # self.home_btn = ctk.CTkButton(
        #     self,
        #     text="Home",
        #     width=120,
        #     height=35,
        #     corner_radius=15,
        #     fg_color="#808080",
        #     hover_color="#696969",
        #     command=self.go_home
        # )
        # self.home_btn.place(relx=0.15, rely=0.92, anchor=CENTER)

        # ===== Dynamic Section Area =====
        self.section_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.section_frame.place(relx=0.5, rely=0.7, anchor=CENTER)

    # ================== CHARGE SECTION ==================
    def show_charge_section(self):
        self.clear_section()

        label = ctk.CTkLabel(
            self.section_frame,
            text="Charging Time (minutes):",
            font=ctk.CTkFont(size=14)
        )
        label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.charge_entry = ctk.CTkEntry(self.section_frame, width=100, placeholder_text="0")
        self.charge_entry.grid(row=0, column=1, padx=10, pady=5)

        disconnect_btn = ctk.CTkButton(
            self.section_frame,
            text="Disconnect",
            width=120,
            height=35,
            corner_radius=15,
            fg_color="#DC143C",
            hover_color="#B22222"
        )
        disconnect_btn.grid(row=1, column=0, columnspan=2, pady=10)

        # Bottom buttons (Home, Start)
        self.show_bottom_buttons(["Home", "Start"])

    # ================== TRIP SECTION ==================
    def show_trip_section(self):
        self.clear_section()

        # Drop Location dropdown
        label1 = ctk.CTkLabel(self.section_frame, text="Drop Location:", font=ctk.CTkFont(size=14))
        label1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.drop_option = ctk.CTkOptionMenu(
            self.section_frame,
            values=["A", "B", "C"]
        )
        self.drop_option.grid(row=0, column=1, padx=10, pady=5)

        # Waiting time
        label2 = ctk.CTkLabel(self.section_frame, text="Waiting Time (minutes):", font=ctk.CTkFont(size=14))
        label2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.wait_entry = ctk.CTkEntry(self.section_frame, width=100, placeholder_text="0")
        self.wait_entry.grid(row=1, column=1, padx=10, pady=5)

        # Loop count
        label3 = ctk.CTkLabel(self.section_frame, text="Loop Count:", font=ctk.CTkFont(size=14))
        label3.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.loop_entry = ctk.CTkEntry(self.section_frame, width=100, placeholder_text="0")
        self.loop_entry.grid(row=2, column=1, padx=10, pady=5)

        # Bottom buttons (Home, Start, Stop)
        self.show_bottom_buttons(["Home", "Start", "Stop"])

    # ================== UTILITIES ==================
    def clear_section(self):
        """Clear all widgets in the section frame"""
        for widget in self.section_frame.winfo_children():
            widget.destroy()

    def show_bottom_buttons(self, labels):
        """Show bottom buttons inside section frame"""
        frame = ctk.CTkFrame(self.section_frame, fg_color="transparent")
        frame.grid(row=10, column=0, columnspan=2, pady=(15, 0))

        for i, name in enumerate(labels):
            btn = ctk.CTkButton(
                frame,
                text=name,
                width=120,
                height=35,
                corner_radius=15,
                fg_color="#1E90FF" if name == "Start" else
                          "#DC143C" if name == "Stop" else
                          "#808080",
                hover_color="#4682B4" if name == "Start" else
                             "#B22222" if name == "Stop" else
                             "#696969",
                command=self.go_home if name == "Home" else None
            )
            btn.grid(row=0, column=i, padx=10)

    def go_home(self):
        self.master.show_home_page()
