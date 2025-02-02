# ui_components/threat_detection.py
import customtkinter as ctk
import tkinter.messagebox as mb
import logging
import random

# Configure logging to display messages on the console.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ThreatDetectionFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Use a vertical layout with each feature in its own section.
        # Optionally, you could use a scrollable frame if the content exceeds the window height.
        self.pack_propagate(False)
        
        # Create each threat detection feature section
        self.create_risk_scoring_section()
        self.create_text_sentiment_section()
        self.create_social_media_scoring_section()
        self.create_dark_web_mentions_section()
        self.create_relationship_network_section()
        self.create_real_time_event_detection_section()
        self.create_user_pattern_tracking_section()
        self.create_automated_alerts_section()
        self.create_bot_fake_detection_section()
    
    def create_risk_scoring_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Risk Scoring Algorithm (Behavior & Affiliations)", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter behavior data:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.risk_entry = ctk.CTkEntry(section, placeholder_text="Type behavior/affiliation info...")
        self.risk_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Calculate Risk", command=self.calculate_risk)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def calculate_risk(self):
        data = self.risk_entry.get()
        # Dummy risk scoring algorithm: use string length modulo a value.
        risk_score = len(data) % 10
        logging.info("Risk Score calculated: %s", risk_score)
        mb.showinfo("Risk Scoring Result", f"Calculated risk score: {risk_score}")
    
    def create_text_sentiment_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Text Sentiment Analysis (NLP Based)", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter text:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.sentiment_entry = ctk.CTkEntry(section, placeholder_text="Type text for analysis...")
        self.sentiment_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Analyze Sentiment", command=self.analyze_sentiment)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def analyze_sentiment(self):
        text = self.sentiment_entry.get()
        # Dummy analysis: positive if "good" is found, negative if "bad", else neutral.
        if "good" in text.lower():
            sentiment = "Positive"
        elif "bad" in text.lower():
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        logging.info("Text Sentiment: %s", sentiment)
        mb.showinfo("Sentiment Analysis Result", f"Sentiment: {sentiment}")
    
    def create_social_media_scoring_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Social Media Activity Scoring", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter username/handle:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.social_entry = ctk.CTkEntry(section, placeholder_text="Username or handle...")
        self.social_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Score Activity", command=self.score_social_media)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def score_social_media(self):
        username = self.social_entry.get()
        # Dummy scoring: use length modulo 10.
        score = len(username) % 10
        logging.info("Social Media Activity Score for '%s': %s", username, score)
        mb.showinfo("Social Media Activity Scoring", f"Score for '{username}': {score}")
    
    def create_dark_web_mentions_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Dark Web Mentions Scoring", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        desc = ctk.CTkLabel(section, text="Click to score dark web mentions:")
        desc.grid(row=1, column=0, padx=5, pady=2)
        
        button = ctk.CTkButton(section, text="Score Dark Web Mentions", command=self.score_dark_web_mentions)
        button.grid(row=2, column=0, padx=5, pady=5)
    
    def score_dark_web_mentions(self):
        # Dummy implementation: random score between 0 and 10.
        score = random.randint(0, 10)
        logging.info("Dark Web Mentions Score: %s", score)
        mb.showinfo("Dark Web Mentions Scoring", f"Score: {score}")
    
    def create_relationship_network_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Relationship Network Analysis (Graph Associations)", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter entity name:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.relationship_entry = ctk.CTkEntry(section, placeholder_text="Entity name...")
        self.relationship_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Analyze Network", command=self.analyze_relationship_network)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def analyze_relationship_network(self):
        entity = self.relationship_entry.get()
        # Dummy implementation just echoes the entity.
        logging.info("Relationship Network Analysis for: %s", entity)
        mb.showinfo("Relationship Network Analysis", f"Analyzed relationships for: {entity}")
    
    def create_real_time_event_detection_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Real-time Event Detection (Live News Analysis)", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        desc = ctk.CTkLabel(section, text="Simulate real-time event detection:")
        desc.grid(row=1, column=0, padx=5, pady=2)
        
        button = ctk.CTkButton(section, text="Start Event Detection", command=self.start_event_detection)
        button.grid(row=2, column=0, padx=5, pady=5)
    
    def start_event_detection(self):
        # Dummy implementation: simply display a message.
        logging.info("Real-time event detection initiated")
        mb.showinfo("Real-time Event Detection", "Real-time event detection started (dummy implementation)")
    
    def create_user_pattern_tracking_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="User Pattern Tracking (Behavior Consistency Check)", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter user identifier:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.pattern_entry = ctk.CTkEntry(section, placeholder_text="User ID/username...")
        self.pattern_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Track User Pattern", command=self.track_user_pattern)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def track_user_pattern(self):
        user_id = self.pattern_entry.get()
        # Dummy scoring based on length.
        score = len(user_id) % 10
        logging.info("User Pattern Tracking for '%s': %s", user_id, score)
        mb.showinfo("User Pattern Tracking", f"Pattern score for '{user_id}': {score}")
    
    def create_automated_alerts_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Automated Alerts (Email, SMS, Push Notifications)", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        email_label = ctk.CTkLabel(section, text="Email:")
        email_label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.alert_email_entry = ctk.CTkEntry(section, placeholder_text="example@example.com")
        self.alert_email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        
        phone_label = ctk.CTkLabel(section, text="Phone:")
        phone_label.grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.alert_phone_entry = ctk.CTkEntry(section, placeholder_text="+123456789")
        self.alert_phone_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Send Test Alert", command=self.send_test_alert)
        button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    def send_test_alert(self):
        email = self.alert_email_entry.get()
        phone = self.alert_phone_entry.get()
        logging.info("Sending test alert to Email: %s, Phone: %s", email, phone)
        mb.showinfo("Automated Alerts", f"Test alert sent to\nEmail: {email}\nPhone: {phone}")
    
    def create_bot_fake_detection_section(self):
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(section, text="Bot & Fake Account Detection (AI-based)", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter account identifier:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.bot_entry = ctk.CTkEntry(section, placeholder_text="Account ID or username...")
        self.bot_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(section, text="Detect Bot/ Fake Account", command=self.detect_bot_fake)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def detect_bot_fake(self):
        account = self.bot_entry.get()
        # Dummy logic: if the length is even, assume detection.
        is_bot = (len(account) % 2 == 0)
        result = "Bot/Fake Account Detected" if is_bot else "No anomalous behavior detected"
        logging.info("Bot & Fake Account Detection for '%s': %s", account, result)
        mb.showinfo("Bot & Fake Account Detection", result)


# For testing purposes: run this module directly.
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.geometry("800x1000")
    app.title("Threat Detection Features")
    threat_frame = ThreatDetectionFrame(app)
    threat_frame.pack(fill="both", expand=True)
    app.mainloop()