# ui_components/security.py
import customtkinter as ctk
import tkinter.messagebox as mb
import logging
import random

# Configure logging for the module.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class SecurityFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Prevent automatic resizing if necessary.
        self.pack_propagate(False)
        
        # Create sections for each security feature.
        self.create_encryption_section()
        self.create_authentication_section()
        self.create_activity_monitoring_section()
        self.create_legal_compliance_section()
        self.create_zero_trust_section()
        self.create_anonymized_processing_section()

    def create_encryption_section(self):
        """Section for Data Encryption (AES-256, Hashicorp Vault)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Data Encryption (AES-256, Hashicorp Vault)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter text to encrypt:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        
        self.encryption_entry = ctk.CTkEntry(section, placeholder_text="Sensitive data...")
        self.encryption_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Encrypt Data", command=self.encrypt_data)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def encrypt_data(self):
        data = self.encryption_entry.get()
        if not data.strip():
            mb.showwarning("Input Error", "Please enter text to encrypt.")
            return
        # Dummy encryption: reverse the text and prepend an "ENC:" tag.
        encrypted = "ENC:" + data[::-1]
        logging.info("Encrypted data: %s", encrypted)
        mb.showinfo("Data Encryption", f"Encrypted Data: {encrypted}")

    def create_authentication_section(self):
        """Section for User Authentication & Access Control (OAuth2, JWT)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="User Authentication & Access Control (OAuth2, JWT)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label1 = ctk.CTkLabel(section, text="Username:")
        label1.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.username_entry = ctk.CTkEntry(section, placeholder_text="Enter username")
        self.username_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        
        label2 = ctk.CTkLabel(section, text="Password:")
        label2.grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.password_entry = ctk.CTkEntry(section, placeholder_text="Enter password", show="*")
        self.password_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Authenticate", command=self.authenticate_user)
        button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Dummy authentication: if password equals "password", authentication passes.
        if username.strip() and password == "password":
            result = f"User '{username}' successfully authenticated using OAuth2/JWT."
        else:
            result = "Authentication failed. Please check your credentials."
        logging.info(result)
        mb.showinfo("User Authentication", result)

    def create_activity_monitoring_section(self):
        """Section for Activity Monitoring & Logging (Prometheus, Grafana)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Activity Monitoring & Logging (Prometheus, Grafana)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        button = ctk.CTkButton(section, text="View Activity Logs", command=self.view_activity_logs)
        button.grid(row=1, column=0, padx=5, pady=5)

    def view_activity_logs(self):
        # Dummy log entries for simulation.
        logs = (
            "Log Entry 1: User login at 10:00 AM\n"
            "Log Entry 2: Data encryption performed at 10:05 AM\n"
            "Log Entry 3: Unauthorized access attempt at 10:20 AM"
        )
        logging.info("Activity logs viewed.")
        mb.showinfo("Activity Logs", logs)

    def create_legal_compliance_section(self):
        """Section for Legal Compliance (GDPR, CCPA)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Legal Compliance (GDPR, CCPA)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        button = ctk.CTkButton(section, text="Check Legal Compliance", command=self.check_compliance)
        button.grid(row=1, column=0, padx=5, pady=5)

    def check_compliance(self):
        # Dummy compliance check using random selection.
        compliance_status = random.choice([
            "Compliant with GDPR & CCPA",
            "Non-compliant: Data processing policies require review"
        ])
        logging.info("Legal compliance check: %s", compliance_status)
        mb.showinfo("Legal Compliance", compliance_status)

    def create_zero_trust_section(self):
        """Section for Zero Trust Architecture (role-based access)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Zero Trust Architecture (Role-based Access)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="User Role:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.role_entry = ctk.CTkEntry(section, placeholder_text="e.g., admin, user")
        self.role_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Apply Zero Trust Check", command=self.zero_trust_check)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def zero_trust_check(self):
        role = self.role_entry.get()
        if role.strip().lower() == "admin":
            result = "Access granted. Admin role verified under Zero Trust Architecture."
        else:
            result = "Access limited. Role-based access control enforced."
        logging.info(result)
        mb.showinfo("Zero Trust Architecture", result)

    def create_anonymized_processing_section(self):
        """Section for Anonymized Data Processing"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Anonymized Data Processing",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter data to anonymize:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.anonymize_entry = ctk.CTkEntry(section, placeholder_text="Sensitive information...")
        self.anonymize_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Anonymize Data", command=self.anonymize_data)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def anonymize_data(self):
        data = self.anonymize_entry.get()
        if not data.strip():
            mb.showwarning("Input Error", "Please enter data to anonymize.")
            return
        # Dummy anonymization: replace all alphanumeric characters with "*".
        anonymized = "".join('*' if c.isalnum() else c for c in data)
        logging.info("Anonymized data: %s", anonymized)
        mb.showinfo("Anonymized Data Processing", f"Result: {anonymized}")


# Standalone testing to run this module directly.
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    app = ctk.CTk()
    app.geometry("800x1000")
    app.title("Security & Compliance Features")
    
    security_frame = SecurityFrame(app)
    security_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    app.mainloop()