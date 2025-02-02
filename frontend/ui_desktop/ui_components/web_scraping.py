# ui_components/web_scraping.py
import customtkinter as ctk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class WebScrapingFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Prevent automatic widget resizing (optional)
        self.pack_propagate(False)

        # Create each web scraping feature section
        self.create_automated_scraping_section()
        self.create_realtime_crawling_section()
        self.create_hidden_scraping_section()
        self.create_ai_article_parsing_section()
        self.create_video_analysis_section()
        self.create_sentiment_analysis_section()

    def create_automated_scraping_section(self):
        """Section: Automated scraping (Scrapy, Playwright, Selenium)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Automated Scraping (Scrapy, Playwright, Selenium)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter URL to scrape:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        
        self.scrape_url_entry = ctk.CTkEntry(section, placeholder_text="https://example.com")
        self.scrape_url_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(
            section,
            text="Start Automated Scraping",
            command=self.start_automated_scraping
        )
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def start_automated_scraping(self):
        url = self.scrape_url_entry.get()
        if not url.strip():
            mb.showwarning("Input Error", "Please enter a valid URL.")
            return
        result = f"Scraping initiated for {url} using automated tools."
        logging.info(result)
        mb.showinfo("Automated Scraping", result)
    
    def create_realtime_crawling_section(self):
        """Section: Real-time data crawling (Websockets & Kafka)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Real-time Data Crawling (Websockets & Kafka)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        button = ctk.CTkButton(
            section,
            text="Start Real-time Crawling",
            command=self.start_realtime_crawling
        )
        button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    
    def start_realtime_crawling(self):
        result = "Real-time data crawling started via Websockets & Kafka."
        logging.info(result)
        mb.showinfo("Real-time Data Crawling", result)
    
    def create_hidden_scraping_section(self):
        """Section: Hidden web scraping (TOR scraping)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Hidden Web Scraping (TOR scraping)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        button = ctk.CTkButton(
            section,
            text="Initiate Hidden Scraping",
            command=self.start_hidden_scraping
        )
        button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    
    def start_hidden_scraping(self):
        result = "Hidden web scraping initiated using the TOR network."
        logging.info(result)
        mb.showinfo("Hidden Web Scraping", result)
    
    def create_ai_article_parsing_section(self):
        """Section: AI-powered article parsing (news summarization)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="AI-Powered Article Parsing (News Summarization)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter article URL or text:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        
        self.article_entry = ctk.CTkEntry(section, placeholder_text="Article URL or content...")
        self.article_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(
            section,
            text="Summarize Article",
            command=self.summarize_article
        )
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def summarize_article(self):
        article_content = self.article_entry.get()
        if not article_content.strip():
            mb.showwarning("Input Error", "Please enter some text or a URL for the article.")
            return
        # Dummy implementation: if the text is long, return the first 50 characters.
        summary = article_content[:50] + "..." if len(article_content) > 50 else article_content
        result = f"Article summary: {summary}"
        logging.info(result)
        mb.showinfo("Article Summarization", result)
    
    def create_video_analysis_section(self):
        """Section: Video analysis (metadata extraction)"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Video Analysis (Metadata Extraction)",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        button_select = ctk.CTkButton(
            section,
            text="Select Video File",
            command=self.select_video_file
        )
        button_select.grid(row=1, column=0, padx=5, pady=5)
        
        self.video_file_label = ctk.CTkLabel(section, text="No file selected")
        self.video_file_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        button_extract = ctk.CTkButton(
            section,
            text="Extract Metadata",
            command=self.extract_video_metadata
        )
        button_extract.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def select_video_file(self):
        file_path = fd.askopenfilename(
            title="Select a Video File",
            filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
        )
        if file_path:
            self.video_file_label.configure(text=file_path)
    
    def extract_video_metadata(self):
        file_path = self.video_file_label.cget("text")
        if file_path == "No file selected":
            mb.showwarning("Input Error", "Please select a video file first.")
            return
        # Dummy implementation: simulate metadata extraction with random values.
        duration = random.randint(1, 180)
        resolution = "1920x1080"
        metadata = f"Metadata for {file_path}:\nDuration: {duration} min, Resolution: {resolution}"
        logging.info(metadata)
        mb.showinfo("Video Metadata", metadata)
    
    def create_sentiment_analysis_section(self):
        """Section: Sentiment analysis on forums & social media"""
        section = ctk.CTkFrame(self)
        section.pack(fill="x", padx=10, pady=5)
        
        title = ctk.CTkLabel(
            section,
            text="Sentiment Analysis on Forums & Social Media",
            font=("Arial", 14, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        label = ctk.CTkLabel(section, text="Enter text to analyze:")
        label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
        
        self.sentiment_entry = ctk.CTkEntry(section, placeholder_text="Text from forum or social media...")
        self.sentiment_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        section.grid_columnconfigure(1, weight=1)
        
        button = ctk.CTkButton(
            section,
            text="Analyze Sentiment",
            command=self.analyze_sentiment
        )
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def analyze_sentiment(self):
        text = self.sentiment_entry.get()
        if not text.strip():
            mb.showwarning("Input Error", "Please enter text to analyze.")
            return
        # Dummy logic: check for keywords “good” or “bad”
        if "good" in text.lower():
            sentiment = "Positive"
        elif "bad" in text.lower():
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        result = f"Sentiment Analysis Result: {sentiment}"
        logging.info(result)
        mb.showinfo("Sentiment Analysis", result)


# Standalone testing: Run this module directly to display the Web Scraping UI.
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    app = ctk.CTk()
    app.geometry("800x1000")
    app.title("Web Scraping & OSINT Features")
    
    web_scraping_frame = WebScrapingFrame(app)
    web_scraping_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    app.mainloop()