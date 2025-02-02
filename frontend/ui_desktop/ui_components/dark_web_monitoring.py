# ui_components/dark_web_monitoring.py
import customtkinter as ctk
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class DarkWebMonitoringFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(self, text="Dark Web Monitoring", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=1, column=0, pady=(10,5))
        monitor_button = ctk.CTkButton(btn_frame, text="Start Monitoring", command=self.perform_monitoring)
        monitor_button.grid(row=0, column=0, padx=5)
        
        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.grid(row=2, column=0, pady=5)
    
    def perform_monitoring(self):
        msg = "Dark web monitoring initiated."
        logging.info(msg)
        self.status_label.configure(text="Monitoring initiated... Check console")
        print(msg)