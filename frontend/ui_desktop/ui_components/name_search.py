# ui_components/name_search.py
import customtkinter as ctk
import logging
import webbrowser
import csv
from difflib import SequenceMatcher

# Versuche, das Modul für Google-Suche zu importieren.
# Falls nicht vorhanden, werden simulierte Treffer verwendet.
try:
    from googlesearch import search
except ImportError:
    search = None

logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class NameSearchFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Gesamt-Layout über grid; Padding wird in den grid()-Aufrufen gesetzt.
        self.grid_columnconfigure(0, weight=1)
        self.current_font_size = 22  # Ausgangswert für Überschriften
        
        # Header-Bereich (enthält Titel, Dark Mode Umschalter, Feedback-Button & Schriftgrößen-Schieber)
        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        self.header_frame.grid_columnconfigure(0, weight=1)
        # Titel
        self.title_label = ctk.CTkLabel(self.header_frame,
                                        text="Namebasierte Suche",
                                        font=("Helvetica", self.current_font_size, "bold"))
        self.title_label.grid(row=0, column=0, sticky="w")
        # Dark Mode Umschalter
        self.mode_switch_var = ctk.BooleanVar(value=False)
        self.mode_switch = ctk.CTkSwitch(self.header_frame, text="Dark Mode", variable=self.mode_switch_var,
                                         command=self.toggle_mode)
        self.mode_switch.grid(row=0, column=1, padx=10)
        # Feedback-Button
        self.feedback_button = ctk.CTkButton(self.header_frame, text="Feedback",
                                             command=self.open_feedback_overlay, corner_radius=8)
        self.feedback_button.grid(row=0, column=2, padx=10)
        # Schriftgrößen-Schieber
        self.font_slider = ctk.CTkSlider(self.header_frame, from_=10, to=30, command=self.change_font_size)
        self.font_slider.set(self.current_font_size)
        self.font_slider.grid(row=0, column=3, padx=10)
        
        # Eingabebereich (z. B. Vorname, Nachname, Aliase, zusätzliche Schlagwörter)
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(0,10))
        self.input_frame.grid_columnconfigure(1, weight=1)
        
        # Vorname (als CTkComboBox für Autovervollständigung; statische Vorschläge)
        self.first_label = ctk.CTkLabel(self.input_frame, text="Vorname:", font=("Helvetica", 14))
        self.first_label.grid(row=0, column=0, sticky="w", padx=(10,5), pady=5)
        self.first_entry = ctk.CTkComboBox(self.input_frame, values=["Max", "Moritz", "Maria", "John", "Anna"])
        self.first_entry.grid(row=0, column=1, sticky="ew", padx=(0,10), pady=5)
        ToolTip(self.first_entry, "Bitte geben Sie den Vornamen ein. Vorschläge: Max, Moritz, Maria, John, Anna.")
        
        # Nachname
        self.last_label = ctk.CTkLabel(self.input_frame, text="Nachname:", font=("Helvetica", 14))
        self.last_label.grid(row=1, column=0, sticky="w", padx=(10,5), pady=5)
        self.last_entry = ctk.CTkEntry(self.input_frame)
        self.last_entry.grid(row=1, column=1, sticky="ew", padx=(0,10), pady=5)
        ToolTip(self.last_entry, "Bitte geben Sie den Nachnamen ein.")
        
        # Aliase
        self.alias_label = ctk.CTkLabel(self.input_frame, text="Aliase (kommagetrennt):", font=("Helvetica", 14))
        self.alias_label.grid(row=2, column=0, sticky="w", padx=(10,5), pady=5)
        self.alias_entry = ctk.CTkEntry(self.input_frame)
        self.alias_entry.grid(row=2, column=1, sticky="ew", padx=(0,10), pady=5)
        ToolTip(self.alias_entry, "Mehrere Aliase bitte mit Komma trennen.")
        
        # Zusätzliche Schlagwörter
        self.extra_label = ctk.CTkLabel(self.input_frame, text="Zusätzliche Schlagwörter:", font=("Helvetica", 14))
        self.extra_label.grid(row=3, column=0, sticky="w", padx=(10,5), pady=5)
        self.extra_entry = ctk.CTkEntry(self.input_frame)
        self.extra_entry.grid(row=3, column=1, sticky="ew", padx=(0,10), pady=5)
        ToolTip(self.extra_entry, "Weitere Suchbegriffe hinzufügen.")
        
        # Filter & Optionen (Checkbuttons)
        self.filter_frame = ctk.CTkFrame(self)
        self.filter_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
        self.filter_frame.grid_columnconfigure((0, 1), weight=1)
        self.filter_title = ctk.CTkLabel(self.filter_frame, text="Filter & Optionen", 
                                         font=("Helvetica", 16, "bold"))
        self.filter_title.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.var_internal = ctk.IntVar(value=1)
        self.var_web = ctk.IntVar(value=1)
        self.var_social = ctk.IntVar(value=1)
        self.var_extended = ctk.IntVar(value=1)
        self.chk_internal = ctk.CTkCheckBox(self.filter_frame, text="Interne Daten", variable=self.var_internal)
        self.chk_internal.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.chk_web = ctk.CTkCheckBox(self.filter_frame, text="Web-Ergebnisse", variable=self.var_web)
        self.chk_web.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        self.chk_social = ctk.CTkCheckBox(self.filter_frame, text="Soziale Netzwerke", variable=self.var_social)
        self.chk_social.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.chk_extended = ctk.CTkCheckBox(self.filter_frame, text="Erweiterte Quellen", variable=self.var_extended)
        self.chk_extended.grid(row=2, column=1, sticky="w", padx=10, pady=5)
        
        # Button-Bereich (Suche starten und Reset)
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=10)
        self.button_frame.grid_columnconfigure((0, 1), weight=1)
        self.search_button = ctk.CTkButton(self.button_frame, text="Suche starten",
                                           command=self.perform_search, corner_radius=8)
        self.search_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.reset_button = ctk.CTkButton(self.button_frame, text="Reset",
                                          command=self.reset_fields, corner_radius=8)
        self.reset_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Fortschritts- und Statusbereich
        self.progress_frame = ctk.CTkFrame(self)
        self.progress_frame.grid(row=4, column=0, sticky="ew", padx=20, pady=10)
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame, width=400)
        self.progress_bar.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.progress_bar.set(0)
        self.status_label = ctk.CTkLabel(self.progress_frame, text="", font=("Helvetica", 14))
        self.status_label.grid(row=0, column=1, padx=10, pady=5)
        
        # Terminal (Protokollierung der Suche)
        self.terminal_label = ctk.CTkLabel(self, text="Suchprotokoll", font=("Helvetica", 16, "bold"))
        self.terminal_label.grid(row=5, column=0, sticky="w", padx=20, pady=(10,5))
        self.terminal_box = ctk.CTkTextbox(self, height=150)
        self.terminal_box.grid(row=6, column=0, padx=20, pady=(0,10), sticky="nsew")
        self.terminal_box.configure(state="disabled")
        
        # Ergebnisse-Bereich (scrollbarer Frame)
        self.results_label = ctk.CTkLabel(self, text="Ergebnisse", font=("Helvetica", 18, "bold"))
        self.results_label.grid(row=7, column=0, sticky="w", padx=20, pady=(10,5))
        self.results_frame = ctk.CTkScrollableFrame(self, height=200)
        self.results_frame.grid(row=8, column=0, padx=20, pady=(0,10), sticky="nsew")
        self.grid_rowconfigure(8, weight=1)
        
        # Export-Button für CSV-Export
        self.export_button = ctk.CTkButton(self, text="Ergebnisse exportieren", 
                                           command=self.export_results, corner_radius=8)
        self.export_button.grid(row=9, column=0, padx=20, pady=(0,10), sticky="ew")
        
        # Notification-Bereich (für temporäre Meldungen)
        self.notification_label = ctk.CTkLabel(self, text="", font=("Helvetica", 14))
        self.notification_label.grid(row=10, column=0, padx=20, pady=(0,10), sticky="ew")
        
        # Liste zur Speicherung der Suchergebnisse
        self.search_results = []
        
        # Detail-Overlay (für Detailansicht eines Ergebnisses; zunächst verborgen)
        self.detail_overlay = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.detail_overlay.place_forget()

    # ------------------------- UI Callback-Methoden -------------------------
    def toggle_mode(self):
        # Umschalter: Dark Mode aktivieren, wenn True; sonst Light Mode.
        if self.mode_switch_var.get():
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def change_font_size(self, value):
        new_size = int(round(float(value)))
        self.current_font_size = new_size
        self.title_label.configure(font=("Helvetica", new_size, "bold"))

    def animate_slide_in(self, widget, start_rel_y, end_rel_y, steps=20, delay=10):
        delta = (end_rel_y - start_rel_y) / steps
        def step(i, current_y):
            if i < steps:
                widget.place_configure(rely=current_y)
                widget.after(delay, lambda: step(i+1, current_y+delta))
            else:
                widget.place_configure(rely=end_rel_y)
        step(0, start_rel_y)

    def show_notification(self, message, duration=3000):
        self.notification_label.configure(text=message)
        self.after(duration, lambda: self.notification_label.configure(text=""))

    def perform_search(self):
        # Suchprotokoll und Ergebnisse leeren
        self.clear_terminal()
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        self.search_results = []
        self.progress_bar.set(0)
        self.status_label.configure(text="Suche wird gestartet...")
        self.update_terminal("Starte Suche ...")
        
        # Suchbegriffe erfassen
        first = self.first_entry.get().strip()
        last = self.last_entry.get().strip()
        aliases = self.alias_entry.get().strip()
        extra = self.extra_entry.get().strip()
        if not (first or last or aliases or extra):
            self.update_terminal("Bitte mindestens einen Suchbegriff eingeben.")
            self.status_label.configure(text="Abbruch: Keine Suchbegriffe.")
            return
        
        search_query = f"{first} {last}"
        if aliases:
            alias_terms = " ".join(a.strip() for a in aliases.split(",") if a.strip())
            search_query += " " + alias_terms
        if extra:
            search_query += " " + extra
        self.update_terminal(f"Suche nach: {search_query}")
        
        # Filter-Aufgaben (simulierte Tasks) basierend auf den Checkbuttons
        tasks = []
        if self.var_internal.get():
            tasks.append(("internal", "Interne Datenbank wird durchsucht...", 800))
        if self.var_web.get():
            tasks.append(("web", "Web-Suchmaschinenabfrage startet...", 1000))
        if self.var_social.get():
            tasks.append(("social", "Soziale Netzwerke werden durchsucht...", 800))
        if self.var_extended.get():
            tasks.append(("extended", "Erweiterte Quellen werden durchsucht...", 800))
        if not tasks:
            self.update_terminal("Es wurden keine Filter ausgewählt!")
            self.status_label.configure(text="Abbruch: Keine Filter.")
            return
        
        self.simulate_tasks(0, tasks, search_query)

    def simulate_tasks(self, index, tasks, query):
        if index < len(tasks):
            task_type, message, delay = tasks[index]
            self.update_terminal(message)
            self.after(delay, lambda: self.process_task(task_type, query, index, tasks))
        else:
            # Alle Tasks abgeschlossen, Ergebnisse sortieren und anzeigen
            sorted_results = self.sort_results_by_accuracy(query, self.search_results)
            self.show_search_results(sorted_results)
            self.update_terminal("Suche abgeschlossen.")
            self.status_label.configure(text="Suche abgeschlossen.")
            self.progress_bar.set(1.0)

    def process_task(self, task_type, query, index, tasks):
        if task_type == "internal":
            res1 = {
                "url": f"https://internal.example.com/profil/{query.replace(' ', '_')}",
                "source": "Interne Datenbank",
                "description": "Ergebnis aus der PeopleFinder-Datenbank."
            }
            res2 = {
                "url": f"https://social.internal.com/user/{query.replace(' ', '')}",
                "source": "Interne Datenbank",
                "description": "Ergebnis aus der SocialSphere-Datenbank."
            }
            self.search_results.extend([res1, res2])
        elif task_type == "web":
            if search is not None:
                try:
                    for url in search(query, num=5, stop=5, pause=1):
                        res = {
                            "url": url,
                            "source": "Web-Suche",
                            "description": "Ergebnis der Suchmaschinenabfrage."
                        }
                        self.search_results.append(res)
                        self.update_terminal(f"Web-Ergebnis: {url}")
                except Exception as e:
                    self.update_terminal(f"Fehler bei Web-Suche: {e}")
                    logging.error("Web-Suche Fehler: %s", e)
            else:
                simulated = [
                    f"https://example.com/profil/{query.replace(' ', '_')}",
                    f"https://news.example.com/articles/{query.replace(' ', '-')}"
                ]
                for url in simulated:
                    res = {
                        "url": url,
                        "source": "Web-Suche (simuliert)",
                        "description": "Simuliertes Web-Ergebnis."
                    }
                    self.search_results.append(res)
                    self.update_terminal(f"Simuliertes Web-Ergebnis: {url}")
        elif task_type == "social":
            simulated_social = [
                f"https://twitter.com/{query.replace(' ', '')}",
                f"https://linkedin.com/in/{query.replace(' ', '-')}"
            ]
            for url in simulated_social:
                res = {
                    "url": url,
                    "source": "Soziale Netzwerke",
                    "description": "Simuliertes Ergebnis aus sozialen Netzwerken."
                }
                self.search_results.append(res)
                self.update_terminal(f"Soziales Ergebnis: {url}")
        elif task_type == "extended":
            simulated_extended = [
                f"https://scholarly.example.com/article/{query.replace(' ', '_')}",
                f"https://press.example.com/mitteilung/{query.replace(' ', '-')}"
            ]
            for url in simulated_extended:
                res = {
                    "url": url,
                    "source": "Erweiterte Quelle",
                    "description": "Ergebnis aus erweiterten Quellen (wissenschaftliche Artikel, Pressemitteilungen)."
                }
                self.search_results.append(res)
                self.update_terminal(f"Erweitertes Ergebnis: {url}")
        
        total = len(tasks)
        self.progress_bar.set((index + 1) / total)
        self.simulate_tasks(index + 1, tasks, query)

    def compute_relevance(self, query, text):
        return SequenceMatcher(None, query.lower(), text.lower()).ratio()

    def sort_results_by_accuracy(self, query, results):
        scored_results = []
        for res in results:
            combined_text = res["url"] + " " + res["source"] + " " + res["description"]
            score = self.compute_relevance(query, combined_text)
            scored_results.append((res, score))
        scored_results.sort(key=lambda x: x[1], reverse=True)
        return scored_results

    def show_search_results(self, sorted_results):
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        if not sorted_results:
            no_result = ctk.CTkLabel(self.results_frame, text="Keine Ergebnisse gefunden.")
            no_result.pack(padx=5, pady=5)
            return
        for res, score in sorted_results:
            txt = f"{res['url']} (Relevanz: {score:.2f})"
            button = ctk.CTkButton(self.results_frame, text=txt, anchor="w",
                                   command=lambda r=res: self.open_detail_overlay(r), corner_radius=8)
            button.pack(padx=5, pady=5, fill="x")

    def open_detail_overlay(self, result):
        # Öffnet ein Overlay (im Hauptfenster) mit Detailinformationen.
        self.detail_overlay.destroy()
        self.detail_overlay = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.detail_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Detailkarte zentriert im Overlay; beginne mit einem Slide-in (von unten)
        detail_card = ctk.CTkFrame(self.detail_overlay, width=500, height=300, 
                                   fg_color="white", corner_radius=10)
        detail_card.place(relx=0.5, rely=1.2, anchor="center")
        self.animate_slide_in(detail_card, start_rel_y=1.2, end_rel_y=0.5, steps=20, delay=15)
        
        title = ctk.CTkLabel(detail_card, text="Detailansicht", font=("Helvetica", 20, "bold"),
                             text_color="#333333")
        title.pack(pady=(20,10))
        # URL
        url_label = ctk.CTkLabel(detail_card, text="URL:", font=("Helvetica", 14, "bold"),
                                 text_color="#333333")
        url_label.pack(pady=(10,0), anchor="w", padx=20)
        url_value = ctk.CTkLabel(detail_card, text=result["url"], font=("Helvetica", 14),
                                 text_color="#333333")
        url_value.pack(pady=(0,10), anchor="w", padx=20)
        # Quelle
        source_label = ctk.CTkLabel(detail_card, text="Quelle:", font=("Helvetica", 14, "bold"),
                                    text_color="#333333")
        source_label.pack(pady=(10,0), anchor="w", padx=20)
        source_value = ctk.CTkLabel(detail_card, text=result["source"], font=("Helvetica", 14),
                                    text_color="#333333")
        source_value.pack(pady=(0,10), anchor="w", padx=20)
        # Beschreibung
        desc_label = ctk.CTkLabel(detail_card, text="Beschreibung:", font=("Helvetica", 14, "bold"),
                                  text_color="#333333")
        desc_label.pack(pady=(10,0), anchor="w", padx=20)
        desc_text = ctk.CTkTextbox(detail_card, height=80, width=460)
        desc_text.pack(pady=(0,10), padx=20)
        desc_text.insert("0.0", result["description"])
        desc_text.configure(state="disabled")
        # Button zum Öffnen im Browser
        open_button = ctk.CTkButton(detail_card, text="Im Browser öffnen",
                                    command=lambda: webbrowser.open(result["url"]), corner_radius=8)
        open_button.pack(pady=(10,5), padx=20, fill="x")
        # Schließen-Button
        close_button = ctk.CTkButton(detail_card, text="Schließen", command=self.close_detail_overlay,
                                     corner_radius=8)
        close_button.pack(pady=(5,20), padx=20, fill="x")

    def close_detail_overlay(self):
        self.detail_overlay.place_forget()

    def open_feedback_overlay(self):
        # Öffnet ein Overlay zur Eingabe von Feedback
        self.feedback_overlay = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.feedback_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        feedback_card = ctk.CTkFrame(self.feedback_overlay, width=500, height=300,
                                     fg_color="white", corner_radius=10)
        feedback_card.place(relx=0.5, rely=1.2, anchor="center")
        self.animate_slide_in(feedback_card, start_rel_y=1.2, end_rel_y=0.5, steps=20, delay=15)
        title = ctk.CTkLabel(feedback_card, text="Feedback", font=("Helvetica", 20, "bold"),
                             text_color="#333333")
        title.pack(pady=(20,10))
        instructions = ctk.CTkLabel(feedback_card, text="Bitte geben Sie Ihr Feedback ein:",
                                    font=("Helvetica", 14), text_color="#333333")
        instructions.pack(pady=(10,5), padx=20, anchor="w")
        self.feedback_textbox = ctk.CTkTextbox(feedback_card, height=100, width=460)
        self.feedback_textbox.pack(pady=(0,10), padx=20)
        send_button = ctk.CTkButton(feedback_card, text="Feedback senden", command=self.send_feedback,
                                    corner_radius=8)
        send_button.pack(pady=(10,5), padx=20, fill="x")
        cancel_button = ctk.CTkButton(feedback_card, text="Abbrechen", command=self.close_feedback_overlay,
                                      corner_radius=8)
        cancel_button.pack(pady=(5,20), padx=20, fill="x")

    def send_feedback(self):
        feedback = self.feedback_textbox.get("1.0", "end").strip()
        if feedback:
            self.update_terminal(f"Feedback erhalten: {feedback}")
            self.show_notification("Feedback gesendet. Vielen Dank!")
        else:
            self.show_notification("Kein Feedback eingegeben.")
        self.close_feedback_overlay()

    def close_feedback_overlay(self):
        if hasattr(self, "feedback_overlay"):
            self.feedback_overlay.destroy()

    def export_results(self):
        if not self.search_results:
            self.update_terminal("Keine Ergebnisse zum Exportieren vorhanden.")
            return
        filename = "name_search_results.csv"
        try:
            with open(filename, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["url", "source", "description"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for res in self.search_results:
                    writer.writerow(res)
            self.update_terminal(f"Ergebnisse wurden erfolgreich nach {filename} exportiert.")
        except Exception as e:
            self.update_terminal(f"Fehler beim Exportieren: {e}")

    def update_terminal(self, message):
        self.terminal_box.configure(state="normal")
        self.terminal_box.insert("end", message + "\n")
        self.terminal_box.see("end")
        self.terminal_box.configure(state="disabled")

    def clear_terminal(self):
        self.terminal_box.configure(state="normal")
        self.terminal_box.delete("1.0", "end")
        self.terminal_box.configure(state="disabled")

    def reset_fields(self):
        self.first_entry.set("")  # Bei CTkComboBox
        self.last_entry.delete(0, "end")
        self.alias_entry.delete(0, "end")
        self.extra_entry.delete(0, "end")
        self.status_label.configure(text="")
        self.clear_terminal()
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        self.progress_bar.set(0)
        self.search_results = []
        self.detail_overlay.place_forget()
        self.show_notification("Felder wurden zurückgesetzt.")

# ------------------------- ToolTip Klasse -------------------------
# Eine einfache Implementierung, die einen kleinen Tooltip beim Überfahren eines Widgets anzeigt.
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.showtip)
        widget.bind("<Leave>", self.hidetip)

    def showtip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 1
        self.tipwindow = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)  # Keine Fensterdekorationen
        tw.wm_geometry("+%d+%d" % (x, y))
        label = ctk.CTkLabel(tw, text=self.text, bg_color="white", text_color="black", corner_radius=4, padx=5, pady=2)
        label.pack()

    def hidetip(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Namebasierte Suche")
    app.geometry("600x1000")
    frame = NameSearchFrame(app)
    frame.pack(fill="both", expand=True)
    app.mainloop()