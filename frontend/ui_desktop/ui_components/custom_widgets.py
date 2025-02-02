import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    """
    A custom button widget extending CTkButton.
    
    This can be further customized as needed.
    """
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)