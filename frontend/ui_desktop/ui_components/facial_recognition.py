# ui_components/facial_recognition.py
import customtkinter as ctk
import tkinter.filedialog as fd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class FacialRecognitionFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(self, text="Facial Recognition Search", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=1, column=0, pady=(10,5))
        select_button = ctk.CTkButton(btn_frame, text="Select Image", command=self.perform_recognition)
        select_button.grid(row=0, column=0, padx=5)
        
        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.grid(row=2, column=0, pady=5)
    
    def perform_recognition(self):
        filename = fd.askopenfilename(
            title="Select an image for facial recognition",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if filename:
            msg = f"Performing facial recognition on: {filename}"
            logging.info(msg)
            self.status_label.configure(text="Recognition initiated... Check console")
            print(msg)