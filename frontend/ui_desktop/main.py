import customtkinter as ctk
import logging

from ui_components.name_search import NameSearchFrame
from ui_components.email_lookup import EmailLookupFrame
from ui_components.phone_lookup import PhoneLookupFrame
from ui_components.social_media_search import SocialMediaSearchFrame
from ui_components.business_financial import BusinessFinancialFrame
from ui_components.criminal_record import CriminalRecordFrame
from ui_components.facial_recognition import FacialRecognitionFrame
from ui_components.dark_web_monitoring import DarkWebMonitoringFrame
from ui_components.geolocation import GeolocationFrame
from ui_components.vehicle_lookup import VehicleLookupFrame
from ui_components.alias_correlation import AliasCorrelationFrame
from ui_components.settings import SettingsFrame

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    app = ctk.CTk()
    app.title("People Search & Intelligence Gathering")
    app.geometry("1200x800")
    
    # Main container holding left navigation and right content area
    main_frame = ctk.CTkFrame(app)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    
    # Left Navigation Panel
    nav_panel = ctk.CTkFrame(main_frame, width=250, corner_radius=8)
    nav_panel.grid(row=0, column=0, sticky="nsw", padx=(0, 10), pady=10)
    
    # Right Content Area where feature UI components are loaded
    content_area = ctk.CTkFrame(main_frame, corner_radius=8)
    content_area.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    
    # Helper function to load a feature UI component into the content area
    def load_feature(frame_class, title_text):
        # Clear previous content in the content area.
        for widget in content_area.winfo_children():
            widget.destroy()
        header = ctk.CTkLabel(content_area, text=title_text, font=("Arial", 18, "bold"))
        header.pack(pady=(10, 20))
        feature_frame = frame_class(content_area)
        feature_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Mapping feature names to their corresponding UI component classes
    features = [
        ("Name Search", NameSearchFrame),
        ("Email Lookup", EmailLookupFrame),
        ("Phone Lookup", PhoneLookupFrame),
        ("Social Media", SocialMediaSearchFrame),
        ("Business & Financial", BusinessFinancialFrame),
        ("Criminal Record", CriminalRecordFrame),
        ("Facial Recognition", FacialRecognitionFrame),
        ("Dark Web Monitoring", DarkWebMonitoringFrame),
        ("Geolocation", GeolocationFrame),
        ("Vehicle Lookup", VehicleLookupFrame),
        ("Alias Correlation", AliasCorrelationFrame),
        ("Settings", SettingsFrame)
    ]
    
    # Create navigation buttons for each feature on the left panel.
    for feature_name, frame_class in features:
        btn = ctk.CTkButton(nav_panel, text=feature_name,
                            command=lambda fc=frame_class, ft=feature_name: load_feature(fc, ft))
        btn.pack(pady=5, padx=10, fill="x")
    
    # Load the default (Name Search) feature on startup.
    load_feature(NameSearchFrame, "Name Search")
    
    app.mainloop()

if __name__ == "__main__":
    main()