# ui_components/phone_lookup.py
import customtkinter as ctk
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class PhoneLookupFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(1, weight=1)
        
        title = ctk.CTkLabel(self, text="Phone Number Lookup", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        phone_label = ctk.CTkLabel(self, text="Phone Number:")
        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = ctk.CTkEntry(self)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        lookup_button = ctk.CTkButton(btn_frame, text="Lookup", command=self.perform_lookup)
        lookup_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_lookup(self):
        phone = self.phone_entry.get()
        msg = f"Looking up phone: {phone}"
        logging.info(msg)
        self.status_label.configure(text="Lookup initiated... Check console")
        print(msg)
    
    def reset_fields(self):
        self.phone_entry.delete(0, "end")
        self.status_label.configure(text="")