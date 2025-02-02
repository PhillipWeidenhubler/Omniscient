import customtkinter as ctk
import tkinter.filedialog as fd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class PeopleSearchFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.pack(fill="both", expand=True)
        
        # Create a Tabview to separate search features
        self.tabview = ctk.CTkTabview(self, width=700)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Add tabs for each feature
        self.tabview.add("Name Search")
        self.tabview.add("Email Lookup")
        self.tabview.add("Phone Lookup")
        self.tabview.add("Social Media")
        self.tabview.add("Business & Financial")
        self.tabview.add("Criminal Record")
        self.tabview.add("Facial Recognition")
        self.tabview.add("Dark Web Monitoring")
        self.tabview.add("Geolocation")
        self.tabview.add("Vehicle Lookup")
        self.tabview.add("Alias Correlation")
        
        # Build each feature's content within its tab
        self.create_name_search(self.tabview.tab("Name Search"))
        self.create_email_lookup(self.tabview.tab("Email Lookup"))
        self.create_phone_lookup(self.tabview.tab("Phone Lookup"))
        self.create_social_media_search(self.tabview.tab("Social Media"))
        self.create_business_financial(self.tabview.tab("Business & Financial"))
        self.create_criminal_record(self.tabview.tab("Criminal Record"))
        self.create_facial_recognition(self.tabview.tab("Facial Recognition"))
        self.create_dark_web_monitoring(self.tabview.tab("Dark Web Monitoring"))
        self.create_geolocation(self.tabview.tab("Geolocation"))
        self.create_vehicle_lookup(self.tabview.tab("Vehicle Lookup"))
        self.create_alias_correlation(self.tabview.tab("Alias Correlation"))
    
    # -------------------------
    # Tab: Name Search
    # -------------------------
    def create_name_search(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Name-based Search", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        first_label = ctk.CTkLabel(parent, text="First Name:")
        first_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.first_entry = ctk.CTkEntry(parent)
        self.first_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        last_label = ctk.CTkLabel(parent, text="Last Name:")
        last_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.last_entry = ctk.CTkEntry(parent)
        self.last_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        alias_label = ctk.CTkLabel(parent, text="Aliases (comma-separated):")
        alias_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.alias_entry = ctk.CTkEntry(parent)
        self.alias_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=(10,5))
        search_button = ctk.CTkButton(btn_frame, text="Search", command=self.perform_name_search)
        search_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_name_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.name_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.name_status.grid(row=5, column=0, columnspan=2, pady=5)
    
    def perform_name_search(self):
        first = self.first_entry.get()
        last = self.last_entry.get()
        aliases = self.alias_entry.get()
        msg = f"Searching for: {first} {last} | Aliases: {aliases}"
        logging.info(msg)
        self.name_status.configure(text="Search initiated... Check console for details")
        print(msg)
        
    def reset_name_fields(self):
        self.first_entry.delete(0, "end")
        self.last_entry.delete(0, "end")
        self.alias_entry.delete(0, "end")
        self.name_status.configure(text="")
    
    # -------------------------
    # Tab: Email Lookup
    # -------------------------
    def create_email_lookup(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Email Lookup", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        email_label = ctk.CTkLabel(parent, text="Email:")
        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ctk.CTkEntry(parent)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        lookup_button = ctk.CTkButton(btn_frame, text="Lookup", command=self.perform_email_lookup)
        lookup_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_email_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.email_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.email_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_email_lookup(self):
        email = self.email_entry.get()
        msg = f"Looking up email: {email}"
        logging.info(msg)
        self.email_status.configure(text="Lookup initiated... Check console for details")
        print(msg)
    
    def reset_email_fields(self):
        self.email_entry.delete(0, "end")
        self.email_status.configure(text="")
    
    # -------------------------
    # Tab: Phone Lookup
    # -------------------------
    def create_phone_lookup(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Phone Number Lookup", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        phone_label = ctk.CTkLabel(parent, text="Phone Number:")
        phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = ctk.CTkEntry(parent)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        lookup_button = ctk.CTkButton(btn_frame, text="Lookup", command=self.perform_phone_lookup)
        lookup_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_phone_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.phone_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.phone_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_phone_lookup(self):
        phone = self.phone_entry.get()
        msg = f"Looking up phone: {phone}"
        logging.info(msg)
        self.phone_status.configure(text="Lookup initiated... Check console for details")
        print(msg)
    
    def reset_phone_fields(self):
        self.phone_entry.delete(0, "end")
        self.phone_status.configure(text="")
    
    # -------------------------
    # Tab: Social Media Search
    # -------------------------
    def create_social_media_search(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Social Media Search", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        username_label = ctk.CTkLabel(parent, text="Username/Handle:")
        username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ctk.CTkEntry(parent)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        search_button = ctk.CTkButton(btn_frame, text="Search", command=self.perform_social_media_search)
        search_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_social_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.social_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.social_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_social_media_search(self):
        username = self.username_entry.get()
        msg = f"Searching social media for: {username}"
        logging.info(msg)
        self.social_status.configure(text="Search initiated... Check console for details")
        print(msg)
    
    def reset_social_fields(self):
        self.username_entry.delete(0, "end")
        self.social_status.configure(text="")
    
    # -------------------------
    # Tab: Business & Financial
    # -------------------------
    def create_business_financial(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Business & Financial Connections", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        business_label = ctk.CTkLabel(parent, text="Business Name:")
        business_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.business_entry = ctk.CTkEntry(parent)
        self.business_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        lookup_button = ctk.CTkButton(btn_frame, text="Lookup", command=self.perform_business_lookup)
        lookup_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_business_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.business_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.business_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_business_lookup(self):
        business = self.business_entry.get()
        msg = f"Looking up business: {business}"
        logging.info(msg)
        self.business_status.configure(text="Lookup initiated... Check console for details")
        print(msg)
    
    def reset_business_fields(self):
        self.business_entry.delete(0, "end")
        self.business_status.configure(text="")
    
    # -------------------------
    # Tab: Criminal Record
    # -------------------------
    def create_criminal_record(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Criminal Record Check", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        name_label = ctk.CTkLabel(parent, text="Full Name:")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.criminal_name_entry = ctk.CTkEntry(parent)
        self.criminal_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        check_button = ctk.CTkButton(btn_frame, text="Check", command=self.perform_criminal_check)
        check_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_criminal_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.criminal_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.criminal_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_criminal_check(self):
        name = self.criminal_name_entry.get()
        msg = f"Checking criminal record for: {name}"
        logging.info(msg)
        self.criminal_status.configure(text="Check initiated... Check console for details")
        print(msg)
    
    def reset_criminal_fields(self):
        self.criminal_name_entry.delete(0, "end")
        self.criminal_status.configure(text="")
    
    # -------------------------
    # Tab: Facial Recognition
    # -------------------------
    def create_facial_recognition(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(parent, text="Facial Recognition Search", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=1, column=0, pady=(10,5))
        select_button = ctk.CTkButton(btn_frame, text="Select Image", command=self.perform_facial_recognition)
        select_button.grid(row=0, column=0, padx=5)
        
        self.facial_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.facial_status.grid(row=2, column=0, pady=5)
    
    def perform_facial_recognition(self):
        filename = fd.askopenfilename(
            title="Select an image for facial recognition",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if filename:
            msg = f"Performing facial recognition on: {filename}"
            logging.info(msg)
            self.facial_status.configure(text="Recognition initiated... Check console for details")
            print(msg)
    
    # -------------------------
    # Tab: Dark Web Monitoring
    # -------------------------
    def create_dark_web_monitoring(self, parent):
        parent.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(parent, text="Dark Web Monitoring", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=1, column=0, pady=(10,5))
        monitor_button = ctk.CTkButton(btn_frame, text="Start Monitoring", command=self.perform_dark_web_monitoring)
        monitor_button.grid(row=0, column=0, padx=5)
        
        self.darkweb_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.darkweb_status.grid(row=2, column=0, pady=5)
    
    def perform_dark_web_monitoring(self):
        msg = "Dark web monitoring initiated."
        logging.info(msg)
        self.darkweb_status.configure(text="Monitoring initiated... Check console for details")
        print(msg)
    
    # -------------------------
    # Tab: Geolocation
    # -------------------------
    def create_geolocation(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Geolocation Tracking", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        ip_label = ctk.CTkLabel(parent, text="IP Address:")
        ip_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.ip_entry = ctk.CTkEntry(parent)
        self.ip_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        lookup_button = ctk.CTkButton(btn_frame, text="Lookup", command=self.perform_geolocation_lookup)
        lookup_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_geolocation_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.geo_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.geo_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_geolocation_lookup(self):
        ip = self.ip_entry.get()
        msg = f"Looking up geolocation for IP: {ip}"
        logging.info(msg)
        self.geo_status.configure(text="Lookup initiated... Check console for details")
        print(msg)
    
    def reset_geolocation_fields(self):
        self.ip_entry.delete(0, "end")
        self.geo_status.configure(text="")
    
    # -------------------------
    # Tab: Vehicle Lookup
    # -------------------------
    def create_vehicle_lookup(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Vehicle Lookup", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        vehicle_label = ctk.CTkLabel(parent, text="License Plate/VIN:")
        vehicle_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.vehicle_entry = ctk.CTkEntry(parent)
        self.vehicle_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        lookup_button = ctk.CTkButton(btn_frame, text="Lookup", command=self.perform_vehicle_lookup)
        lookup_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_vehicle_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.vehicle_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.vehicle_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_vehicle_lookup(self):
        vehicle = self.vehicle_entry.get()
        msg = f"Looking up vehicle: {vehicle}"
        logging.info(msg)
        self.vehicle_status.configure(text="Lookup initiated... Check console for details")
        print(msg)
    
    def reset_vehicle_fields(self):
        self.vehicle_entry.delete(0, "end")
        self.vehicle_status.configure(text="")
    
    # -------------------------
    # Tab: Alias Correlation
    # -------------------------
    def create_alias_correlation(self, parent):
        parent.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(parent, text="Online Alias Correlation", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        alias_label = ctk.CTkLabel(parent, text="Alias:")
        alias_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.alias_correlation_entry = ctk.CTkEntry(parent)
        self.alias_correlation_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,5))
        correlate_button = ctk.CTkButton(btn_frame, text="Correlate", command=self.perform_alias_correlation)
        correlate_button.grid(row=0, column=0, padx=5)
        reset_button = ctk.CTkButton(btn_frame, text="Reset", command=self.reset_alias_fields)
        reset_button.grid(row=0, column=1, padx=5)
        
        self.alias_status = ctk.CTkLabel(parent, text="", fg_color="transparent")
        self.alias_status.grid(row=3, column=0, columnspan=2, pady=5)
    
    def perform_alias_correlation(self):
        alias = self.alias_correlation_entry.get()
        msg = f"Correlating alias: {alias}"
        logging.info(msg)
        self.alias_status.configure(text="Correlation initiated... Check console for details")
        print(msg)
    
    def reset_alias_fields(self):
        self.alias_correlation_entry.delete(0, "end")
        self.alias_status.configure(text="")

# If you want to test the PeopleSearchFrame in a standalone window,
# uncomment the lines below.

# if __name__ == "__main__":
#     ctk.set_appearance_mode("System")  # Options: "System" (default), "Dark", "Light"
#     ctk.set_default_color_theme("blue")
#     root = ctk.CTk()
#     root.title("People Search & Intelligence Gathering")
#     root.geometry("900x700")
#     PeopleSearchFrame(root)
#     root.mainloop()