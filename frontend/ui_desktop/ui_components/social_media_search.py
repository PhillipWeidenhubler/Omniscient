# ui_components/social_media_search.py
import customtkinter as ctk
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class SocialMediaSearchFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(1, weight=1)
        
        title = ctk.CTkLabel(self, text="Social Media Search", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        username_label = ctk.CTkLabel(self, text="Username/Handle:")
        username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        search_button = ctk.CTkButton(btn_frame, text="Search", command=self.perform_search)
        search_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_search(self):
        username = self.username_entry.get()
        msg = f"Searching social media for: {username}"
        logging.info(msg)
        self.status_label.configure(text="Search initiated... Check console")
        print(msg)
    
    def reset_fields(self):
        self.username_entry.delete(0, "end")
        self.status_label.configure(text="")