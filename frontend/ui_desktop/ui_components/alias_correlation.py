# ui_components/alias_correlation.py
import customtkinter as ctk
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class AliasCorrelationFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(1, weight=1)
        
        title = ctk.CTkLabel(self, text="Online Alias Correlation", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        alias_label = ctk.CTkLabel(self, text="Alias:")
        alias_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.alias_entry = ctk.CTkEntry(self)
        self.alias_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        correlate_button = ctk.CTkButton(btn_frame, text="Correlate", command=self.perform_correlation)
        correlate_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_correlation(self):
        alias = self.alias_entry.get()
        msg = f"Correlating alias: {alias}"
        logging.info(msg)
        self.status_label.configure(text="Correlation initiated... Check console")
        print(msg)
    
    def reset_fields(self):
        self.alias_entry.delete(0, "end")
        self.status_label.configure(text="")